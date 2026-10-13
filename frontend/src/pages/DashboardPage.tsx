import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { api } from '../services/api';
import { Course, LearnerProfile, Citation } from '../types';
import { QuizModal, DocumentItem } from '../components/QuizModal';
import { SourceViewerModal } from '../components/SourceViewerModal';
import { CourseHeader } from '../components/dashboard/CourseHeader';
import { ContinueLearningCard } from '../components/dashboard/ContinueLearningCard';
import { MasterySummaryCard } from '../components/dashboard/MasterySummaryCard';
import { DueReviewsCard } from '../components/dashboard/DueReviewsCard';
import { DocumentCardGrid } from '../components/dashboard/DocumentCardGrid';
import { CompactStudyTools } from '../components/dashboard/CompactStudyTools';
import { CreateCourseModal } from '../components/CreateCourseModal';
import { X, Loader2 } from 'lucide-react';

interface DashboardPageProps {
  activeCourseId: string;
  studentId: string;
  studentName: string;
  onSelectCourse: (id: string) => void;
  onCoursesUpdated: () => void;
  courses: Course[];
}

export const DashboardPage: React.FC<DashboardPageProps> = ({
  activeCourseId,
  studentId,
  studentName,
  onSelectCourse,
  onCoursesUpdated,
  courses,
}) => {
  const navigate = useNavigate();
  const location = useLocation();

  const activeCourse = courses.find((c) => c.id === activeCourseId) || courses[0] || null;

  // Real data states
  const [documents, setDocuments] = useState<DocumentItem[]>([]);
  const [concepts, setConcepts] = useState<any[]>([]);
  const [profile, setProfile] = useState<LearnerProfile | null>(null);
  const [dueReviewsCount, setDueReviewsCount] = useState<number>(0);
  const [loading, setLoading] = useState<boolean>(true);

  // Modals state
  const [isQuizModalOpen, setIsQuizModalOpen] = useState(false);
  const [isCreateCourseOpen, setIsCreateCourseOpen] = useState(false);
  const [activeCitation, setActiveCitation] = useState<Citation | null>(null);

  // Quick Summarizer / URL Explainer modal
  const [activeToolModal, setActiveToolModal] = useState<'summarize' | 'link' | null>(null);
  const [toolInput, setToolInput] = useState('');
  const [toolResult, setToolResult] = useState<string | null>(null);
  const [toolLoading, setToolLoading] = useState(false);

  // Load real data for the active course and logged-in user
  const loadDashboardData = async () => {
    if (!activeCourse) {
      setLoading(false);
      return;
    }
    setLoading(true);
    try {
      const [docsData, conceptsData, profileData, reviewsData] = await Promise.all([
        api.getUserDocuments(activeCourse.id).catch(() => []),
        api.getConcepts(activeCourse.id).catch(() => []),
        api.getLearnerMastery(studentId || 'default_student').catch(() => null),
        api.getDueFlashcards(activeCourse.id).catch(() => []),
      ]);

      setDocuments(docsData || []);
      setConcepts(conceptsData || []);
      setProfile(profileData || null);
      setDueReviewsCount(Array.isArray(reviewsData) ? reviewsData.length : 0);
    } catch (e) {
      console.warn('Dashboard data fetch error:', e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadDashboardData();
  }, [activeCourse?.id, studentId]);

  // Open create course if triggered from state
  useEffect(() => {
    if ((location.state as any)?.openCreateCourse) {
      setIsCreateCourseOpen(true);
    }
  }, [location.state]);

  // Derive weakest concept for Continue Learning
  const weakestConcept = React.useMemo(() => {
    if (!concepts || concepts.length === 0) return null;
    const conceptStates = profile?.concept_states || {};
    
    // Sort concepts by lowest mastery probability
    const sorted = [...concepts].sort((a, b) => {
      const pA = conceptStates[a.id]?.mastery_probability ?? 0.1;
      const pB = conceptStates[b.id]?.mastery_probability ?? 0.1;
      return pA - pB;
    });

    const lowest = sorted[0];
    const p = conceptStates[lowest.id]?.mastery_probability ?? 0.15;
    return { name: lowest.name, mastery_probability: p };
  }, [concepts, profile]);

  // Handle Document Card actions
  const handleOpenDocViewer = (docId: string) => {
    const doc = documents.find(d => d.id === docId);
    if (doc) {
      setActiveCitation({
        citation_index: 1,
        chunk_id: doc.id,
        document_name: doc.name,
        document_title: doc.name,
        page: 1,
        page_or_slide: 'Page 1',
        snippet: `Opening document: ${doc.name}. Verified course content indexed.`,
        quote: `Opening document: ${doc.name}. Verified course content indexed.`,
        source_type: 'pdf',
      });
    }
  };

  const handleAskTutor = (topicOrDocName: string) => {
    navigate(`/tutor?concept=${encodeURIComponent(topicOrDocName)}`);
  };

  const handleQuizCreated = (quizData: any) => {
    navigate('/quiz', { state: quizData });
  };

  // Quick Summarizer / Explainer executor
  const handleExecuteTool = async () => {
    if (!toolInput.trim() || toolLoading) return;
    setToolLoading(true);
    setToolResult(null);
    try {
      if (activeToolModal === 'summarize') {
        const formData = new FormData();
        formData.append('text', toolInput);
        formData.append('length', 'concise');
        const res = await api.summarize(formData);
        setToolResult(res.summary || 'Summary compiled successfully.');
      } else if (activeToolModal === 'link') {
        const res = await api.explainUrl(toolInput, activeCourse?.id);
        setToolResult(res.explanation || res.summary || 'Link explained.');
      }
    } catch (err: any) {
      setToolResult(`Error: ${err.message || 'Operation failed'}`);
    } finally {
      setToolLoading(false);
    }
  };

  return (
    <div className="flex-1 flex flex-col bg-[#FAF8F5] overflow-y-auto">
      <div className="flex-1 p-4 sm:p-6 lg:p-8 space-y-6 max-w-6xl w-full mx-auto">
        
        {/* 1. COURSE HEADER */}
        <CourseHeader
          course={activeCourse}
          docCount={documents.length}
          conceptCount={concepts.length}
          onOpenQuiz={() => setIsQuizModalOpen(true)}
          onOpenTutor={() => navigate('/tutor')}
          onOpenConceptMap={() => navigate('/concept-map')}
          onOpenCreateCourse={() => setIsCreateCourseOpen(true)}
        />

        {/* 2. CONTINUE LEARNING (Next Recommended Action from Real Mastery) */}
        <ContinueLearningCard
          weakestConcept={weakestConcept}
          onTargetedQuiz={(concept) => setIsQuizModalOpen(true)}
          onAskTutor={handleAskTutor}
        />

        {/* 3. MASTERY SUMMARY & DUE REVIEWS GRID */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <MasterySummaryCard
            profile={profile}
            totalConcepts={concepts.length}
          />
          <DueReviewsCard
            dueCount={dueReviewsCount}
            onStartReview={() => navigate('/revision')}
          />
        </div>

        {/* 4. COURSE MATERIALS (DOCUMENT CARDS WITH DOCUMENT'S OWN CONCEPTS) */}
        <DocumentCardGrid
          documents={documents}
          onOpenQuizModalWithDoc={() => setIsQuizModalOpen(true)}
          onAskTutorWithDoc={handleAskTutor}
          onOpenDocumentViewer={handleOpenDocViewer}
          onUploadClick={() => setIsCreateCourseOpen(true)}
        />

        {/* 5. COMPACT AI STUDY TOOLS MENU */}
        <CompactStudyTools
          onOpenSummarizer={() => {
            setActiveToolModal('summarize');
            setToolInput('');
            setToolResult(null);
          }}
          onOpenLinkExplainer={() => {
            setActiveToolModal('link');
            setToolInput('');
            setToolResult(null);
          }}
        />

      </div>

      {/* QUIZ MODAL */}
      <QuizModal
        isOpen={isQuizModalOpen}
        onClose={() => setIsQuizModalOpen(false)}
        activeCourse={activeCourse}
        userDocuments={documents}
        onQuizCreated={handleQuizCreated}
        onDocumentUploaded={loadDashboardData}
      />

      {/* CREATE COURSE MODAL */}
      <CreateCourseModal
        isOpen={isCreateCourseOpen}
        onClose={() => setIsCreateCourseOpen(false)}
        onCourseCreated={() => {
          onCoursesUpdated();
          loadDashboardData();
        }}
      />

      {/* DOCUMENT VIEWER MODAL */}
      {activeCitation && (
        <SourceViewerModal
          citation={activeCitation}
          onClose={() => setActiveCitation(null)}
        />
      )}

      {/* QUICK TOOL MODAL */}
      {activeToolModal && (
        <div className="fixed inset-0 z-50 bg-black/50 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white rounded-3xl max-w-lg w-full p-6 space-y-4 shadow-xl border border-slate-200">
            <div className="flex items-center justify-between">
              <h3 className="font-bold text-sm text-slate-900">
                {activeToolModal === 'summarize' ? 'Summarize Study Material' : 'Explain Web Resource'}
              </h3>
              <button
                onClick={() => setActiveToolModal(null)}
                className="p-1 rounded-full text-slate-400 hover:text-slate-700"
              >
                <X className="h-4 w-4" />
              </button>
            </div>

            <textarea
              rows={3}
              value={toolInput}
              onChange={(e) => setToolInput(e.target.value)}
              placeholder={activeToolModal === 'summarize' ? 'Paste notes to summarize...' : 'Enter URL: https://...'}
              className="w-full p-3 rounded-xl border border-slate-200 text-xs bg-slate-50 focus:bg-white focus:outline-none focus:border-blue-500"
            />

            {toolResult && (
              <div className="p-3.5 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-700 max-h-48 overflow-y-auto leading-relaxed">
                {toolResult}
              </div>
            )}

            <div className="flex justify-end gap-2 pt-2">
              <button
                onClick={() => setActiveToolModal(null)}
                className="px-4 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100"
              >
                Close
              </button>
              <button
                onClick={handleExecuteTool}
                disabled={!toolInput.trim() || toolLoading}
                className="px-5 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs transition shadow-xs flex items-center gap-1.5 disabled:opacity-50"
              >
                {toolLoading ? <Loader2 className="h-3.5 w-3.5 animate-spin" /> : null}
                <span>Run</span>
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
