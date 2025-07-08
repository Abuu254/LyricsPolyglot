from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, songs, vocab, recordings, flashcards
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.1.0",
    description="Learn Korean through interactive song lyrics"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(songs.router, prefix="/api/songs", tags=["songs"])
app.include_router(vocab.router, prefix="/api/vocab", tags=["vocab"])
app.include_router(recordings.router, prefix="/api/recordings", tags=["recordings"])
app.include_router(flashcards.router, prefix="/api/flashcards", tags=["flashcards"])

@app.get("/")
async def root():
    return {"message": "Welcome to LyricsPolyglot API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}