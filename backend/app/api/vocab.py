from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class VocabResponse(BaseModel):
    word: str
    definition: str
    pronunciation: str
    audio_url: Optional[str] = None

@router.get("/define", response_model=VocabResponse)
async def define_word(word: str):
    # Placeholder implementation - return mock definitions
    mock_definitions = {
        "안녕하세요": {
            "word": "안녕하세요",
            "definition": "Hello (formal)",
            "pronunciation": "annyeonghaseyo",
            "audio_url": "https://example.com/audio/annyeonghaseyo.mp3"
        },
        "반갑습니다": {
            "word": "반갑습니다",
            "definition": "Nice to meet you",
            "pronunciation": "bangapseumnida",
            "audio_url": "https://example.com/audio/bangapseumnida.mp3"
        },
        "오늘": {
            "word": "오늘",
            "definition": "Today",
            "pronunciation": "oneul",
            "audio_url": "https://example.com/audio/oneul.mp3"
        }
    }

    if word in mock_definitions:
        return mock_definitions[word]
    else:
        raise HTTPException(status_code=404, detail="Word not found")