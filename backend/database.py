import json
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from backend.config import DB_PATH

Base = declarative_base()
engine = create_engine(f"sqlite:///{DB_PATH}", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class ExamModel(Base):
    __tablename__ = "exams"

    id = Column(String(64), primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    total_questions = Column(Integer, default=120)
    duration_minutes = Column(Integer, default=150)
    source = Column(String(64), default="benchmark") # 'benchmark' or 'langgraph_generated'
    exam_type = Column(String(32), default="vact") # 'vact' or 'spt'
    subject = Column(String(64), nullable=True) # for SPT: 'math', 'english', etc.
    max_score = Column(Float, default=1200.0) # 1200.0 for V-ACT, 10.0 for SPT
    created_at = Column(DateTime, default=datetime.utcnow)
    data_json = Column(Text, nullable=False) # JSON string of questions

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "total_questions": self.total_questions,
            "duration_minutes": self.duration_minutes,
            "source": self.source,
            "exam_type": self.exam_type or "vact",
            "subject": self.subject,
            "max_score": self.max_score or (10.0 if self.exam_type == "spt" else 1200.0),
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "questions": json.loads(self.data_json) if self.data_json else []
        }

class UserModel(Base):
    __tablename__ = "users"

    id = Column(String(64), primary_key=True, index=True)
    username = Column(String(64), unique=True, index=True, nullable=False)
    password_hash = Column(String(256), nullable=False)
    full_name = Column(String(128), nullable=False)
    role = Column(String(32), default="student") # "admin" hoặc "student"
    student_class = Column(String(64), nullable=True) # Ví dụ: "12A1"
    school = Column(String(128), nullable=True)        # Ví dụ: "THPT Chuyên"
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "full_name": self.full_name,
            "role": self.role or "student",
            "student_class": self.student_class or "",
            "school": self.school or "",
            "created_at": self.created_at.isoformat() if self.created_at else None
        }

class SubmissionModel(Base):
    __tablename__ = "submissions"

    id = Column(String(64), primary_key=True, index=True)
    user_id = Column(String(64), nullable=True, index=True) # Khóa ngoại liên kết UserModel
    exam_id = Column(String(64), nullable=False, index=True)
    candidate_name = Column(String(128), default="Thí sinh ĐGNL")
    started_at = Column(DateTime, default=datetime.utcnow)
    submitted_at = Column(DateTime, default=datetime.utcnow)
    time_spent_seconds = Column(Integer, default=0)
    
    # Scores
    total_score = Column(Float, default=0.0) # Thang 1200
    sec1_score = Column(Float, default=0.0)  # Thang 400
    sec2_score = Column(Float, default=0.0)  # Thang 300
    sec3_score = Column(Float, default=0.0)  # Thang 500
    
    # Detailed answers & analytics (JSON)
    answers_json = Column(Text, nullable=False)
    results_json = Column(Text, nullable=False)
    radar_data_json = Column(Text, nullable=False)
    ai_advice = Column(Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "exam_id": self.exam_id,
            "candidate_name": self.candidate_name,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "submitted_at": self.submitted_at.isoformat() if self.submitted_at else None,
            "time_spent_seconds": self.time_spent_seconds,
            "total_score": round(self.total_score, 1),
            "sec1_score": round(self.sec1_score, 1),
            "sec2_score": round(self.sec2_score, 1),
            "sec3_score": round(self.sec3_score, 1),
            "answers": json.loads(self.answers_json) if self.answers_json else {},
            "results": json.loads(self.results_json) if self.results_json else {},
            "radar_data": json.loads(self.radar_data_json) if self.radar_data_json else {},
            "ai_advice": self.ai_advice
        }

def init_db():
    Base.metadata.create_all(bind=engine)
    try:
        with engine.connect() as conn:
            cursor = conn.connection.cursor()
            cursor.execute("PRAGMA table_info(exams)")
            columns = [row[1] for row in cursor.fetchall()]
            if "exam_type" not in columns:
                cursor.execute("ALTER TABLE exams ADD COLUMN exam_type VARCHAR(32) DEFAULT 'vact'")
            if "subject" not in columns:
                cursor.execute("ALTER TABLE exams ADD COLUMN subject VARCHAR(64)")
            if "max_score" not in columns:
                cursor.execute("ALTER TABLE exams ADD COLUMN max_score FLOAT DEFAULT 1200.0")
            
            # Cập nhật migration cho bảng submissions nếu thiếu user_id
            cursor.execute("PRAGMA table_info(submissions)")
            sub_columns = [row[1] for row in cursor.fetchall()]
            if "user_id" not in sub_columns:
                cursor.execute("ALTER TABLE submissions ADD COLUMN user_id VARCHAR(64)")

            # Cập nhật migration cho bảng users nếu thiếu role
            cursor.execute("PRAGMA table_info(users)")
            user_columns = [row[1] for row in cursor.fetchall()]
            if "role" not in user_columns:
                cursor.execute("ALTER TABLE users ADD COLUMN role VARCHAR(32) DEFAULT 'student'")

            conn.connection.commit()
    except Exception as e:
        print(f"Database migration note: {e}")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
