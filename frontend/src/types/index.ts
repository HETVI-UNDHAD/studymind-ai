export interface CourseUnit {
  id: string;
  course_id: string;
  unit_number: number;
  title: string;
  description?: string;
}

export interface Course {
  id: string;
  name: string;
  description?: string;
  subject?: string;
  semester?: string;
  exam_date?: string;
  created_at: string;
  units?: CourseUnit[];
  document_count: number;
  chunk_count?: number;
  topic_count: number;
  concept_count: number;
  overall_mastery: number;
  topics?: any[];
  concepts?: any[];
}

export interface DocumentItem {
  id: string;
  course_id: string;
  filename: string;
  file_type: 'pdf' | 'slide' | 'video' | 'audio' | 'image' | string;
  file_size?: number;
  page_count?: number;
  slide_count?: number;
  duration_seconds?: number;
  status: 'pending' | 'processing' | 'processed' | 'error';
  created_at: string;
}

export interface VisualElement {
  id: string;
  document_id: string;
  course_id: string;
  element_type: string;
  page_number?: number;
  slide_number?: number;
  caption: string;
  structured_description: string;
  image_url?: string;
}

export interface Citation {
  citation_index: number;
  source_type: 'pdf' | 'slide' | 'video' | 'image' | 'link' | string;
  document_name: string;
  document_title?: string;
  source_document?: string;
  page_number?: number;
  slide_number?: number;
  page_or_slide?: string;
  page?: number;
  timestamp_start?: number;
  timestamp_end?: number;
  bbox?: number[]; // [x0, y0, x1, y1]
  keyframe_path?: string;
  visual_frame_summary?: string;
  snippet: string;
  quote?: string;
  chunk_id: string;
  visual_description?: string;
}

export interface ClaimVerification {
  claim: string;
  supported: boolean;
  source_doc?: string;
  citation_index?: number;
  reason?: string;
}

export interface ExternalLink {
  title: string;
  url: string;
  source: string;
  snippet?: string;
}

export interface AnswerSegment {
  text: string;
  citations: Citation[];
  type: 'sourced' | 'outside';
}

export interface ChatMessage {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  grounded?: boolean;
  is_outside_knowledge?: boolean;
  refused?: boolean;
  refusal?: boolean;
  refusal_category?: string;
  check_yourself_question?: string;
  answer_segments?: AnswerSegment[];
  citations?: Citation[];
  external_links?: ExternalLink[];
  confidence_score?: number;
  follow_ups?: string[];
  verification_question?: string;
  claims_verification?: ClaimVerification[];
  unsupported_claims?: string[];
  timestamp: string;
  interactive_quiz?: {
    question_id: string;
    question_text: string;
    options: string[];
    correct_answer: string;
    explanation: string;
    concept_id?: string;
    user_selected?: string;
    is_correct?: boolean;
    xp_awarded?: number;
  };
}

export interface Question {
  id: string;
  course_id: string;
  concept_id?: string;
  question_text: string;
  question_type: string;
  difficulty: 'Easy' | 'Medium' | 'Hard' | string;
  options?: string[];
  correct_answer: string;
  explanation: string;
  source_document: string;
  source_location: string;
  source_chunk_id?: string;
  question_hash?: string;
  verification_status?: string;
  verification_details?: any;
}

export interface Assessment {
  id: string;
  course_id: string;
  title: string;
  topic_name?: string;
  total_questions: number;
  difficulty: string;
  time_limit_minutes: number;
  status: 'pending' | 'in_progress' | 'completed';
  score: number;
  auto_submitted?: boolean;
  safe_mode_violation?: string;
  questions: Question[];
  created_at: string;
}

export interface AnswerFeedback {
  question_id: string;
  question_text: string;
  student_answer: string;
  correct_answer: string;
  is_correct: boolean;
  explanation: string;
  source_document: string;
  source_location: string;
  likely_misconception?: string;
  concept_name: string;
  difficulty: string;
}

export interface AssessmentReport {
  assessment_id: string;
  total_questions: number;
  correct_count: number;
  score_percentage: number;
  time_spent_seconds: number;
  auto_submitted?: boolean;
  safe_mode_violation?: string;
  topic_performance: Record<string, number>;
  difficulty_performance: Record<string, number>;
  weak_concepts: string[];
  detected_misconceptions: string[];
  recommended_next_step: {
    action: string;
    details: string;
    practice_recs: Array<{ count: number; difficulty: string; topic: string }>;
  };
  detailed_feedbacks: AnswerFeedback[];
}

export interface LearnerMasteryRecord {
  concept_id: string;
  concept_name: string;
  topic_name: string;
  mastery_probability: number;
  confidence: number;
  attempt_count: number;
  correct_count: number;
  incorrect_count: number;
  status: 'Mastered' | 'Developing' | 'Needs Attention';
  last_review?: string;
}

export interface LearnerProfile {
  student_id: string;
  concept_states?: Record<string, any>;
  overall_mastery: number;
  overall_mastery_pct: number;
  topics_mastered_count: number;
  concepts_mastered_count: number;
  topics_needing_revision_count: number;
  questions_answered_total: number;
  current_study_streak_days: number;
  assessment_accuracy: number;
  attempt_history: Array<{ date: string; accuracy: number; attempts: number }>;
  source_coverage_percentage: number;
  mastery_by_concept: LearnerMasteryRecord[];
  weak_topics: Array<{ topic_name: string; mastery: number; concept_count: number }>;
  recommendations: Array<{
    concept_id: string;
    concept_name: string;
    target_concept: string;
    current_mastery: number;
    recommendation_type: string;
    reason: string;
    estimated_minutes: number;
    action_label: string;
  }>;
}

export interface EvaluationMetrics {
  faithfulness: number;
  answer_relevancy: number;
  context_precision: number;
  context_recall: number;
  citation_accuracy: number;
  unsupported_rate: number;
  question_verification_rate: number;
  question_repetition_rate: number;
  false_refusal_rate?: number;
  bkt_auc?: number;
  bkt_log_loss?: number;
  total_test_cases: number;
  evaluated_at: string;
  is_live_measurement: boolean;
  test_results: Array<{
    case_id: string;
    question: string;
    type: string;
    result: string;
    details: string;
    grounded: boolean;
  }>;
  simulation_results?: Array<{
    student_id: string;
    archetype: string;
    initial_mastery: number;
    final_mastery: number;
    mastery_gain: number;
    sessions: Array<{ session: string; mastery_pct: number; questions_attempted: number }>;
  }>;
}
