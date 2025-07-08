from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to LyricsPolyglot API"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_get_song():
    response = client.get("/api/songs/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Dynamite"
    assert data["artist"] == "BTS"

def test_get_song_lyrics():
    response = client.get("/api/songs/1/lyrics")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert "word" in data[0]
    assert "start_ms" in data[0]
    assert "end_ms" in data[0]