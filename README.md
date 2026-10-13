# StudyMind AI

StudyMind AI is a source-grounded tutoring and adaptive learning platform. It allows students and instructors to upload lecture slides, PDF textbooks, notes, and video recordings, and then study with an AI tutor that strictly cites course material down to exact pages, slide numbers, and timestamps.

The platform also includes Bayesian Knowledge Tracing (BKT) to model student concept mastery, prerequisite-gated concept maps, verified practice assessments, and spaced repetition revision tools.

---

## Key Features

- **Multimodal Document Ingestion**: Upload course materials in various formats:
  - PDFs with bounding-box citations (`[x0, y0, x1, y1]`)
  - PowerPoint presentations (`.pptx` / `.ppt`) with slide previews and instructor notes
  - Lecture video and audio recordings (`.mp4`, `.mp3`) with Whisper transcription and OpenCV slide change detection
- **Strictly Grounded AI Tutor**:
  - Direct answers citing specific pages, slides, or timestamps
  - Calibrated refusal guard: alerts the student if a question is outside the course syllabus rather than hallucinating
  - Interactive in-chat checkpoint quizzes with instant answer feedback and explanation
  - Voice tutor mode with speech-to-text and audio readout
- **Adaptive Quiz & Assessment Engine**:
  - Automatically synthesizes practice questions from course excerpts
  - Validates questions using multi-model solving, sympy math verification, and distractor checks
  - Proctored safe-mode exam interface with fullscreen lock, timer, and question review bookmarks
- **Bayesian Knowledge Tracing (BKT) & Concept Map**:
  - Tracks individual concept mastery ($P(L)$) in real time based on quiz attempts
  - Directed Acyclic Graph (DAG) visualizing prerequisite relationships
  - Prerequisite gating: locks advanced topics until foundational concepts reach $\ge 60\%$ mastery
- **Revision Center & Study Planner**:
  - High-yield summary cards and formula cheat sheets
  - Spaced repetition scheduling based on Ebbinghaus forgetting curves

---

## Tech Stack

- **Backend**: Python 3.11+, FastAPI, Uvicorn, NetworkX, SymPy, PyMuPDF, python-pptx, OpenCV
- **AI & Embeddings**: Groq API (`qwen/qwen3.8-27b`), HuggingFace Sentence Transformers (`all-MiniLM-L6-v2`), Faster-Whisper
- **Frontend**: React 19, TypeScript, Vite, Tailwind CSS, Lucide React, Framer Motion
- **Database & Auth**: Supabase (PostgreSQL + Auth + Storage), with automatic fallback to local JSON database for development

---

## Getting Started

### Prerequisites

- Python 3.11 or higher
- Node.js 18 or higher & npm
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/HETVI-UNDHAD/studymind-ai.git
cd studymind-ai
```

### 2. Backend Setup

1. Create and activate a Python virtual environment:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS / Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create your `.env` file from `.env.example`:
   ```bash
   cp .env.example .env
   ```
   Add your API keys in `.env` (Groq API key, Supabase credentials if using Supabase).

4. Start the FastAPI backend:
   ```bash
   python -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
   ```
   The backend API will be running at `http://localhost:8000`. API documentation is available at `http://localhost:8000/docs`.

### 3. Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install npm dependencies:
   ```bash
   npm install
   ```

3. Start the Vite development server:
   ```bash
   npm run dev
   ```
   The application will be accessible at `http://localhost:5173`.

---

## Project Structure

```text
studymind-ai/
├── backend/
│   ├── app/
│   │   ├── api/            # FastAPI routes and endpoints
│   │   ├── assessment/     # Quiz generation, verification & scoring
│   │   ├── core/           # Config, settings, error definitions
│   │   ├── ingestion/      # PDF, PPTX, Video/Whisper pipeline
│   │   ├── learner/        # Bayesian Knowledge Tracing (BKT) engine
│   │   ├── providers/      # LLM, Vision, STT & Embedding providers
│   │   ├── rag/            # Hybrid search (Dense + BM25) and RRF grounding
│   │   ├── services/       # Database manager (Supabase / local JSON)
│   │   └── main.py         # Application entry point
│   └── data/               # Schemas and local data storage
├── frontend/
│   ├── src/
│   │   ├── components/     # UI components, modals, tutor chat, layout
│   │   ├── context/        # Auth and application state
│   │   ├── pages/          # Dashboard, Tutor, Quiz, Concept Map, Files
│   │   ├── services/       # API client services
│   │   └── types/          # TypeScript interface definitions
│   ├── package.json
│   └── vite.config.ts
├── tests/                  # Automated pytest test suites
├── requirements.txt        # Python dependencies
└── README.md
```

---

## Testing

Run the test suite to verify backend pipelines:

```bash
pytest tests/ -v
```

To run the frontend production build check:

```bash
cd frontend
npm run build
```

---

## License

This project is licensed under the MIT License.