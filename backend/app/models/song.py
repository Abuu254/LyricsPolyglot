from sqlmodel import SQLModel, Field
from typing import Optional, List
from datetime import datetime

class Song(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    artist: str
    album: Optional[str] = None
    album_art_url: Optional[str] = None
    provider_id: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class LyricLine(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    song_id: int = Field(foreign_key="song.id")
    word: str
    start_ms: int
    end_ms: int
    line_number: int