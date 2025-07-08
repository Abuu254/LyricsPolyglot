from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from pydantic import BaseModel

router = APIRouter()

class SongResponse(BaseModel):
    id: int
    title: str
    artist: str
    album: str = None
    album_art_url: str = None
    provider_id: str = None

class LyricLineResponse(BaseModel):
    word: str
    start_ms: int
    end_ms: int

@router.get("/{song_id}", response_model=SongResponse)
async def get_song(song_id: int):
    # Placeholder implementation - return mock data
    if song_id == 1:
        return {
            "id": 1,
            "title": "Dynamite",
            "artist": "BTS",
            "album": "Dynamite (DayTime Version)",
            "album_art_url": "https://example.com/dynamite.jpg",
            "provider_id": "spotify:track:123456"
        }
    else:
        raise HTTPException(status_code=404, detail="Song not found")

@router.get("/{song_id}/lyrics", response_model=List[LyricLineResponse])
async def get_song_lyrics(song_id: int):
    # Placeholder implementation - return mock lyrics
    if song_id == 1:
        return [
            {"word": "안녕하세요", "start_ms": 0, "end_ms": 2000},
            {"word": "반갑습니다", "start_ms": 2000, "end_ms": 4000},
            {"word": "오늘도", "start_ms": 4000, "end_ms": 5000},
            {"word": "좋은", "start_ms": 5000, "end_ms": 6000},
            {"word": "하루", "start_ms": 6000, "end_ms": 8000},
        ]
    else:
        raise HTTPException(status_code=404, detail="Song lyrics not found")