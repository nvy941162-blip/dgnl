from typing import TypedDict, List, Dict, Any, Optional

class QuestionItem(TypedDict):
    question_number: int
    section_id: str
    domain: str
    difficulty: str
    prompt: str
    options: Dict[str, str]
    correct_answer: str
    explanation: str
    passage: Optional[str]
    chart_image: Optional[str]

class CouncilEvaluation(TypedDict):
    passed: bool
    critic_notes: str
    distractor_score: float # 0 to 1.0 (độ bẫy của 3 phương án nhiễu)
    single_truth_verified: bool

class AgentCouncilState(TypedDict):
    # Inputs
    topic: str
    section_target: str # "all", "language", "logic_data", or "problem_solving"
    count: int
    difficulty: str # "medium", "hard", "mixed"
    
    # RAG & HyDE
    hypothetical_doc: str
    retrieved_contexts: List[str]
    ragas_faithfulness: float
    ragas_relevance: float
    
    # Generated questions
    draft_questions: List[Dict[str, Any]]
    
    # Critic agent feedback
    critic_evaluations: List[Dict[str, Any]]
    final_questions: List[Dict[str, Any]]
    
    # Logs & Timeline
    agent_logs: List[Dict[str, str]]
    error: Optional[str]
