#!/usr/bin/env python3
"""
Seed script to populate the database with initial demo data
"""

import asyncio
from sqlmodel import SQLModel, create_engine, Session
from app.models.song import Song, LyricLine
from app.core.config import settings

async def seed_database():
    """Seed the database with demo song and lyrics"""

    # Create engine
    engine = create_engine(settings.DATABASE_URL)

    # Create tables
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        # Create demo song
        demo_song = Song(
            title="Dynamite",
            artist="BTS",
            album="Dynamite (DayTime Version)",
            album_art_url="https://example.com/dynamite.jpg",
            provider_id="spotify:track:123456"
        )
        session.add(demo_song)
        session.commit()
        session.refresh(demo_song)

        # Create demo lyrics
        demo_lyrics = [
            LyricLine(song_id=demo_song.id, word="안녕하세요", start_ms=0, end_ms=2000, line_number=1),
            LyricLine(song_id=demo_song.id, word="반갑습니다", start_ms=2000, end_ms=4000, line_number=1),
            LyricLine(song_id=demo_song.id, word="오늘도", start_ms=4000, end_ms=5000, line_number=2),
            LyricLine(song_id=demo_song.id, word="좋은", start_ms=5000, end_ms=6000, line_number=2),
            LyricLine(song_id=demo_song.id, word="하루", start_ms=6000, end_ms=8000, line_number=2),
        ]

        for lyric in demo_lyrics:
            session.add(lyric)

        session.commit()
        print(f"Seeded database with song '{demo_song.title}' and {len(demo_lyrics)} lyric lines")

if __name__ == "__main__":
    asyncio.run(seed_database())