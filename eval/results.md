# Quantitative Evaluation Benchmark Results

**Execution Runtime:** 151.64s across 30 test cases  
**Target Course:** `a091a4aa-a333-4a0c-85ec-9af9ad8505bd` (Parallelism And Distributed Data Processing Notes: Theory & Applications)  
**Evaluated At:** 2026-10-12 14:38:11 UTC  

## 1. Overall Performance Summary

| Metric | Measured Score | Target Benchmark | Status |
| :--- | :---: | :---: | :---: |
| **RAGAS Faithfulness** | `1.000` | `>= 0.850` | PASS |
| **RAGAS Answer Relevancy** | `0.768` | `>= 0.850` | REVIEW |
| **RAGAS Context Precision** | `0.091` | `>= 0.800` | REVIEW |
| **RAGAS Context Recall** | `0.000` | `>= 0.850` | REVIEW |
| **Citation Accuracy** | `0.769` | `>= 0.900` | REVIEW |
| **Unsupported Refusal Rate** | `1.000` | `>= 0.850` | PASS |
| **False Refusal Rate** | `0.818` | `<= 0.150` | REVIEW |
| **Quiz Verification Rate** | `1.000` | `>= 0.900` | PASS |
| **BKT AUC** | `0.753` | `>= 0.700` | PASS |
| **BKT Log-Loss** | `0.776` | `<= 0.650` | REVIEW |

## 2. Test Cases Breakdown (30 Golden Items)

| Case ID | Question Type | Grounded | Result | Citations | Details |
| :--- | :--- | :---: | :--- | :---: | :--- |
| `dyn_eval_01` | source_answerable | Yes | Passed | 3 | Generated cited answer (3 citations) with 100% claim support. |
| `dyn_eval_02` | source_answerable | No | Failed (False Refusal) | 0 | Mistakenly refused answerable course question. |
| `dyn_eval_03` | source_answerable | No | Failed (False Refusal) | 0 | Mistakenly refused answerable course question. |
| `dyn_eval_04` | source_answerable | No | Failed (False Refusal) | 0 | Mistakenly refused answerable course question. |
| `dyn_eval_05` | source_answerable | Yes | Passed | 4 | Generated cited answer (4 citations) with 100% claim support. |
| `dyn_eval_06` | source_answerable | No | Failed (False Refusal) | 0 | Mistakenly refused answerable course question. |
| `dyn_eval_07` | source_answerable | No | Failed (False Refusal) | 0 | Mistakenly refused answerable course question. |
| `dyn_eval_08` | source_answerable | No | Failed (False Refusal) | 0 | Mistakenly refused answerable course question. |
| `dyn_eval_09` | source_answerable | No | Failed (False Refusal) | 0 | Mistakenly refused answerable course question. |
| `dyn_eval_10` | source_answerable | No | Failed (False Refusal) | 0 | Mistakenly refused answerable course question. |
| `dyn_eval_11` | source_answerable | No | Failed (False Refusal) | 0 | Mistakenly refused answerable course question. |
| `dyn_eval_12` | source_answerable | No | Failed (False Refusal) | 0 | Mistakenly refused answerable course question. |
| `dyn_eval_13` | source_answerable | Yes | Passed | 2 | Generated cited answer (2 citations) with 100% claim support. |
| `dyn_eval_14` | source_answerable | No | Failed (False Refusal) | 0 | Mistakenly refused answerable course question. |
| `dyn_eval_15` | source_answerable | No | Failed (False Refusal) | 0 | Mistakenly refused answerable course question. |
| `dyn_eval_16` | source_answerable | No | Failed (False Refusal) | 0 | Mistakenly refused answerable course question. |
| `dyn_eval_17` | source_answerable | No | Failed (False Refusal) | 0 | Mistakenly refused answerable course question. |
| `dyn_eval_18` | source_answerable | Yes | Passed | 4 | Generated cited answer (4 citations) with 100% claim support. |
| `dyn_unsupported_19` | unsupported | No | Passed (Refused) | 0 | Correctly refused off-syllabus query with confidence gate. |
| `dyn_unsupported_20` | unsupported | No | Passed (Refused) | 0 | Correctly refused off-syllabus query with confidence gate. |
| `dyn_unsupported_21` | unsupported | No | Passed (Refused) | 0 | Correctly refused off-syllabus query with confidence gate. |
| `dyn_unsupported_22` | unsupported | No | Passed (Refused) | 0 | Correctly refused off-syllabus query with confidence gate. |
| `dyn_unsupported_23` | unsupported | No | Passed (Refused) | 0 | Correctly refused off-syllabus query with confidence gate. |
| `dyn_unsupported_24` | unsupported | No | Passed (Refused) | 0 | Correctly refused off-syllabus query with confidence gate. |
| `dyn_unsupported_25` | unsupported | No | Passed (Refused) | 0 | Correctly refused off-syllabus query with confidence gate. |
| `dyn_unsupported_26` | unsupported | No | Passed (Refused) | 0 | Correctly refused off-syllabus query with confidence gate. |
| `dyn_video_27` | video | No | Failed (False Refusal) | 0 | Mistakenly refused answerable course question. |
| `dyn_video_28` | video | No | Failed (False Refusal) | 0 | Mistakenly refused answerable course question. |
| `dyn_visual_29` | visual | No | Failed (False Refusal) | 0 | Mistakenly refused answerable course question. |
| `dyn_visual_30` | visual | No | Failed (False Refusal) | 0 | Mistakenly refused answerable course question. |

## 3. Honest Error Analysis & Failure Modes

Total error cases identified: **18** / 30 items.

| Case ID | Type | Question | Failure Reason |
| :--- | :--- | :--- | :--- |
| `dyn_eval_02` | source_answerable | What key relationships does the material discuss regarding What? | Mistakenly refused answerable course question. |
| `dyn_eval_03` | source_answerable | What key relationships does the material discuss regarding Hadoop? | Mistakenly refused answerable course question. |
| `dyn_eval_04` | source_answerable | What key relationships does the material discuss regarding Master? | Mistakenly refused answerable course question. |
| `dyn_eval_06` | source_answerable | What key relationships does the material discuss regarding Flexibility? | Mistakenly refused answerable course question. |
| `dyn_eval_07` | source_answerable | What key relationships does the material discuss regarding HDFS? | Mistakenly refused answerable course question. |
| `dyn_eval_08` | source_answerable | What key relationships does the material discuss regarding Task? | Mistakenly refused answerable course question. |
| `dyn_eval_09` | source_answerable | What key relationships does the material discuss regarding Blocks? | Mistakenly refused answerable course question. |
| `dyn_eval_10` | source_answerable | What key relationships does the material discuss regarding Example? | Mistakenly refused answerable course question. |
| `dyn_eval_11` | source_answerable | What key relationships does the material discuss regarding Apache? | Mistakenly refused answerable course question. |
| `dyn_eval_12` | source_answerable | What key relationships does the material discuss regarding Name? | Mistakenly refused answerable course question. |
| `dyn_eval_14` | source_answerable | What key relationships does the material discuss regarding Replication? | Mistakenly refused answerable course question. |
| `dyn_eval_15` | source_answerable | What key relationships does the material discuss regarding Note? | Mistakenly refused answerable course question. |
| `dyn_eval_16` | source_answerable | What key relationships does the material discuss regarding Rack? | Mistakenly refused answerable course question. |
| `dyn_eval_17` | source_answerable | What key relationships does the material discuss regarding Considering? | Mistakenly refused answerable course question. |
| `dyn_video_27` | video | What key visual demonstration is shown during the video lecture presentation? | Mistakenly refused answerable course question. |
| `dyn_video_28` | video | Explain the step-by-step experiment recorded in the lecture video demonstration. | Mistakenly refused answerable course question. |
| `dyn_visual_29` | visual | How does the architectural diagram illustrate the component relationships? | Mistakenly refused answerable course question. |
| `dyn_visual_30` | visual | Interpret the structural schematic figure shown in the slide deck. | Mistakenly refused answerable course question. |

### Concrete Failure Modes & Remediations

1. **Out-of-Scope Query Boundary:**
   - *Observation:* Off-syllabus queries correctly trigger refusal based on calibrated cosine threshold (0.68).
   - *Remediation:* Maintained Refusal Calibration script to tune the gate per course chunks.

2. **Multimodal Diagram Grounding:**
   - *Observation:* Visual figures require cross-referencing visual captions with textual chunks.
   - *Remediation:* Visual elements table stores extracted bounding boxes, captions, and source document coordinates.

3. **Knowledge Tracing Convergence:**
   - *Observation:* BKT parameters require empirical bounds to prevent over-confidence on sparse observations.
   - *Remediation:* BKT engine dynamically scales transit and guess parameters with difficulty weighting.
