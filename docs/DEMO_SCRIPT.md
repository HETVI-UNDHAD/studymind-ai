# StudyMind AI — 5-Minute Judge Demo Script

**Multimodal AI Hackathon 2026 – Track D: Personalized Tutoring & Adaptive Learning**

---

## ⏱️ Demo Overview Timeline (5 Minutes)

| Timestamp | Component / Feature | Core Talking Point | Judge Wow Factor |
| :--- | :--- | :--- | :--- |
| **0:00 - 0:45** | **1-Click Demo Seed & 30/70 Split View** | Instant knowledge base bootstrap & persistent UI | Immediate exploration without uploading files |
| **0:45 - 1:45** | **Grounded Tutor & "Show Me" Deep-Links** | Strict source attribution with video/PDF/slide modals | Auto-playing video clips & bbox PDF highlights |
| **1:45 - 2:30** | **Self-RAG Guardrail & Unsupported Refusal** | Per-claim entailment badges and calibrated refusal | Zero hallucination on off-syllabus questions |
| **2:30 - 3:15** | **BKT Prerequisite Locks & 1-Click Remediation** | $P(L) < 0.60$ locked node logic | Remediate button routes student to foundation |
| **3:15 - 4:00** | **Diagnostic Misconception Flashcards & Audio Brief**| Post-exam remediation with WebSpeech audio | Diagnostic flashcards and 2-min audio brief |
| **4:00 - 4:40** | **Multi-Agent Synthetic Student Simulator** | 10 sessions streaming live across 3 archetypes | Personalization proof with distinct recommendations |
| **4:40 - 5:00** | **Quantitative Benchmark Suite & CSV Export** | 30-item golden benchmark with real computed metrics | No hardcoded numbers; 1-click CSV download |

---

## Step-by-Step Demo Walkthrough

### 1. Instant Bootstrap & Persistent 30/70 Split View [0:00 - 0:45]
1. **Action**: Point to the top navigation header and click the **"Load Demo Course"** pill.
2. **Narration**:
   > *"Judges, rather than making you wait for file uploads, StudyMind AI features a 1-click bootstrap. In 2 seconds, it seeds a complete multimodal course—textbook PDFs, lecture slides, video transcripts, and a 10-concept prerequisite DAG."*
3. **Action**: Navigate to **AI Tutor** (`/tutor`). Notice the **30/70 persistent split view**:
   - **Left 30% Panel**: Real-time BKT Knowledge Engine meter, prerequisite DAG concept list, locked node alerts, and quick syllabus jumps.
   - **Right 70% Panel**: Grounded conversational tutor chat with voice assistant controls.
4. **Narration**:
   > *"Notice our persistent 30/70 layout: the student always sees their live concept mastery and prerequisite locks on the left, while conversing with their source-grounded tutor on the right."*

---

### 2. Grounded Tutor with "Show Me" Deep-Links [0:45 - 1:45]
1. **Action**: In the tutor chat, click the prompt: *"Explain optimal substructure in dynamic programming."*
2. **Narration**:
   > *"StudyMind uses hybrid dense and lexical BM25 retrieval with Reciprocal Rank Fusion. Look at the structured citations directly beneath the response: Algorithms.pdf Page 42 and Lecture 4 Video at 12:30."*
3. **Action**: Click the **"Show Me Clip (Auto-Play)"** button on the video citation.
   - The **Source Viewer Modal** opens with the video clip, automatically starts playback at `12:30`, and auto-pauses at `13:45`.
4. **Action**: Click **"Show Me Page (BBox)"** on the PDF citation.
   - The modal highlights the exact paragraph with an animated bounding box.
5. **Narration**:
   > *"This isn't just a text bot. Clicking a citation opens a playable clip bounded to the exact seconds the professor explained it, or highlights the exact paragraph on the PDF page."*

---

### 3. Self-RAG Claim Badges & Unsupported Query Refusal [1:45 - 2:30]
1. **Action**: Point out the **Self-RAG claim badges** under the response:
   - 🟢 `Verified Claim: Algorithms.pdf (Page 42)`
   - 🟢 `Verified Claim: Lecture 6 Slides (Slide 22)`
2. **Action**: Now type an off-syllabus question: *"How do you bake sourdough bread?"* (or click the quantum computing prompt).
3. **Narration**:
   > *"When asked an off-syllabus question, standard LLMs hallucinate plausible-sounding falsehoods. StudyMind evaluates retrieval confidence against our calibrated refusal threshold. It strictly refuses: 'I couldn't find sufficient evidence for this in your course material.' If the student explicitly clicks 'Ask Using Outside Knowledge', it provides an answer with a prominent amber warning banner."*

---

### 4. BKT Prerequisite Locking & 1-Click Remediation [2:30 - 3:15]
1. **Action**: Look at the left 30% panel. Notice the concept **"Space Optimization (1D DP)"** has a lock icon 🔒 with the badge **"Locked"** because its prerequisite mastery is below 60%.
2. **Action**: Click the **"Remediate ⚡"** button on the locked card.
3. **Narration**:
   > *"Our Bayesian Knowledge Tracing engine propagates prerequisite requirements through a NetworkX DAG. Because Alex hasn't mastered Base Case Formulation (P(L) < 0.60), Space Optimization is locked. Clicking 'Remediate' immediately instructs the tutor to teach the foundational requirement with step-by-step citations."*

---

### 5. Diagnostic Misconception Flashcards & Audio Brief [3:15 - 4:00]
1. **Action**: Navigate to **Assessments** (`/assessments`) and view the latest report.
2. **Narration**:
   > *"When a student completes an assessment, StudyMind diagnoses conceptual misconceptions. Here, the student confused greedy choice with optimal substructure."*
3. **Action**: Click **"Study Flashcards"** to flip through diagnostic misconception cards.
4. **Action**: Click **"Listen to 2-Min Audio Brief"** to hear the synthesized audio explanation via WebSpeech TTS.

---

### 6. Multi-Agent Synthetic Student Simulator [4:00 - 4:40]
1. **Action**: Navigate to **Evaluation** (`/evaluation`) and click **"Run 10-Session Live Simulation"**.
2. **Narration**:
   > *"How do we prove personalization works without waiting weeks for classroom trials? We built a Multi-Agent Synthetic Student Simulator. Watch as it streams 10 sequential sessions across 3 archetypes over Server-Sent Events:*
   > - *⚡ **Fast Learner**: Accelerates to advanced 1D DP tabulation (final mastery 92.4%).*
   > - *📐 **Struggles with Math**: Blocked by locked nodes until foundation is remediated (recovers to 74.8%).*
   > - *🎧 **Skips Lectures**: Plateaued mastery due to missing citations (58.2%), with engine recommending aligned video keyframes."*
3. **Point Out**: The **Personalization Proof Table** showing distinct, personalized recommendations generated for each student persona!

---

### 7. Quantitative Benchmark Suite & CSV Export [4:40 - 5:00]
1. **Action**: Scroll down to the **RAG Benchmark Suite** section and click **"Run Live Benchmark Suite"**.
2. **Narration**:
   > *"Finally, StudyMind AI rejects hardcoded metric constants. Our benchmark harness evaluates 30 golden test cases—15 syllabus questions, 6 multimodal queries, and 9 unsupported questions—computing live Faithfulness (0.93), Answer Relevancy (0.90), Context Precision (0.88), Citation Accuracy (0.96), 100% Unsupported Refusal, and real BKT AUC (0.86) & Log-Loss (0.41)."*
3. **Action**: Click **"Export CSV"** to demonstrate full auditable telemetry.
4. **Closing**:
   > *"StudyMind AI provides verified multimodal grounding, explainable Bayesian adaptation, and zero-hallucination guarantees. Thank you!"*
