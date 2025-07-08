from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime

router = APIRouter()

class Flashcard(BaseModel):
    id: int
    word: str
    definition: str
    pronunciation: str
    due_date: datetime
    interval: int
    ease_factor: float

class GradeRequest(BaseModel):
    grade: int  # 1-5 scale

@router.get("/today", response_model=List[Flashcard])
async def get_todays_flashcards():
    # Placeholder implementation - return mock flashcards
    return [
        {
            "id": 1,
            "word": "안녕하세요",
            "definition": "Hello (formal)",
            "pronunciation": "annyeonghaseyo",
            "due_date": datetime.utcnow(),
            "interval": 1,
            "ease_factor": 2.5
        },
        {
            "id": 2,
            "word": "감사합니다",
            "definition": "Thank you",
            "pronunciation": "kamsahamnida",
            "due_date": datetime.utcnow(),
            "interval": 3,
            "ease_factor": 2.3
        }
    ]

@router.post("/{flashcard_id}/grade")
async def grade_flashcard(flashcard_id: int, grade: GradeRequest):
    # Placeholder implementation - update SRS algorithm
    return {
        "flashcard_id": flashcard_id,
        "grade": grade.grade,
        "next_review": "2024-01-15T10:00:00Z",
        "interval": 5,
        "ease_factor": 2.4
    }