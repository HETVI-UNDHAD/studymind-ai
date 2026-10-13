import os
import tempfile
import uuid
import pytest
from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.services.database import db
from backend.app.ingestion.pipeline import ingestion_pipeline as pipeline
from tests.conftest import make_test_auth_headers

client = TestClient(app)

def test_no_static_data():
    """
    DYNAMIC-ONLY ACCEPTANCE TEST (Requirement 10 & Phase 1 Strengthened):
    1. Start with an empty user account with zero existing records.
    2. Assert every GET endpoint returns empty or zero values (NOT sample data / demo algorithms).
    3. Ingest a document on an unrelated subject (Marine Biology - Coral Reef Ecosystems).
    4. Assert concepts are non-empty AND each concept name or definition overlaps the uploaded text.
    5. Assert grounded answer has valid citation and off-topic question is refused.
    """
    student_id = f"dynamic_student_{uuid.uuid4().hex[:10]}"
    headers = make_test_auth_headers(student_id)

    # 1. Verify isolated clean state for this student
    courses_res = client.get("/api/courses", headers=headers)
    assert courses_res.status_code == 200
    user_courses = courses_res.json()
    assert len(user_courses) == 0, f"Expected 0 courses for clean student, found {len(user_courses)}"

    mastery_res = client.get(f"/api/learner/{student_id}/mastery", headers=headers)
    assert mastery_res.status_code == 200
    mastery_data = mastery_res.json()
    assert len(mastery_data.get("mastery_by_concept", [])) == 0
    assert mastery_data.get("overall_mastery", 0.0) == 0.0

    rec_res = client.get(f"/api/learner/{student_id}/recommendations", headers=headers)
    assert rec_res.status_code == 200
    assert len(rec_res.json().get("recommendations", [])) == 0

    flash_res = client.get(f"/api/learner/{student_id}/flashcards/due", headers=headers)
    assert flash_res.status_code == 200
    assert len(flash_res.json().get("flashcards", [])) == 0

    # 2. Create a course on an unrelated subject (Marine Biology)
    course_payload = {
        "name": "Marine Biology & Coral Ecology",
        "subject": "Biology",
        "description": "Studies of marine reef ecosystems, zooxanthellae endosymbiosis, and calcification."
    }
    create_res = client.post("/api/courses", json=course_payload, headers=headers)
    assert create_res.status_code == 200
    course = create_res.json()
    course_id = course["id"]
    assert course["name"] == "Marine Biology & Coral Ecology"

    # 3. Create and ingest a text document on Marine Biology
    doc_text = (
        "Coral reefs are formed by marine invertebrates belonging to the class Anthozoa. "
        "Reef-building stony corals secrete calcium carbonate skeletons that form the structural foundation. "
        "Crucially, corals maintain an obligate endosymbiotic relationship with photosynthetic dinoflagellates called zooxanthellae. "
        "Zooxanthellae provide up to 90 percent of the coral's energy through photosynthesis, while the coral host provides inorganic nutrients and shelter. "
        "Thermal stress induces coral bleaching, where corals expel their symbiotic zooxanthellae, leading to starvation and eventual mortality if elevated sea surface temperatures persist."
    )

    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False, mode="w", encoding="utf-8") as tmp:
        tmp.write(doc_text)
        tmp_path = tmp.name

    try:
        process_res = pipeline.process_file(course_id, tmp_path, "coral_reef_ecology.txt")
        assert process_res["status"] in ["completed", "processed"]

        # 4. Verify concepts extracted match Marine Biology and overlap the uploaded text
        detail_res = client.get(f"/api/courses/{course_id}", headers=headers)
        assert detail_res.status_code == 200
        detail = detail_res.json()

        assert len(detail.get("documents", [])) >= 1
        assert any("coral" in d["filename"].lower() for d in detail["documents"])

        # Check concepts: must be non-empty and overlap uploaded text
        concepts = db.list_all("concepts", lambda c: c.get("course_id") == course_id)
        assert len(concepts) > 0, "Expected non-empty concepts extracted from uploaded document"

        doc_text_lower = doc_text.lower()
        for c in concepts:
            c_name = c.get("name", "").lower()
            c_desc = (c.get("description") or "").lower()
            name_words = [w for w in c_name.replace("-", " ").split() if len(w) > 3]
            desc_words = [w for w in c_desc.split() if len(w) > 4]
            name_overlap = any(w in doc_text_lower for w in name_words)
            desc_overlap = any(w in doc_text_lower for w in desc_words)
            assert name_overlap or desc_overlap, f"Concept '{c_name}' does not overlap uploaded text: {c_desc}"

        # Must NOT contain Computer Science topics
        concept_names = [c["name"].lower() for c in concepts]
        assert not any("dynamic programming" in cn or "dijkstra" in cn or "knapsack" in cn for cn in concept_names)

        # 5. Query tutor for the course
        tutor_res = client.post("/api/tutor/query", json={
            "course_id": course_id,
            "query": "What is the role of zooxanthellae in coral reefs?",
            "allow_outside_knowledge": False
        }, headers=headers)
        assert tutor_res.status_code == 200
        tutor_data = tutor_res.json()
        assert tutor_data.get("grounded") is True
        assert len(tutor_data.get("citations", [])) >= 1
        assert "coral" in tutor_data["citations"][0]["document_name"].lower()

        # 6. Verify off-topic question refuses factually
        refusal_res = client.post("/api/tutor/query", json={
            "course_id": course_id,
            "query": "How do I build a dynamic programming knapsack table in Java?",
            "allow_outside_knowledge": False
        }, headers=headers)
        assert refusal_res.status_code == 200
        ref_data = refusal_res.json()
        assert ref_data.get("refused") is True or ref_data.get("grounded") is False
        assert len(ref_data.get("citations", [])) == 0

    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
