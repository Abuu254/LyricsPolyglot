# LyricsPolyglot 🎵

Learn Korean through interactive, time-synced song lyrics with AI-powered pronunciation feedback.

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/lyricspolyglot.git
cd lyricspolyglot

# 2. Start all services
docker compose up --build -d

# 3. Access the application
open http://localhost:3000    # Frontend
open http://localhost:8000/docs  # API Documentation
```

## 📋 Project Overview

LyricsPolyglot is a web application that helps users learn Korean through interactive song lyrics. The app features:

- **Time-synced lyrics**: Lyrics highlight in real-time as the song plays
- **Pronunciation scoring**: AI-powered feedback on Korean pronunciation
- **Spaced repetition**: Flashcards for vocabulary retention
- **Interactive learning**: Click words to see definitions and hear pronunciation

## 🏗️ Architecture

### Frontend
- **Next.js 14** with React 18
- **Tailwind CSS** for styling
- **React Query** for data fetching
- **Zustand** for state management
- **WaveSurfer.js** for audio visualization

### Backend
- **FastAPI** with Python 3.11
- **SQLModel** for database models
- **PostgreSQL** for data storage
- **Redis** for caching and sessions
- **Celery** for background tasks

### AI Services
- **Google Cloud Speech-to-Text** for Korean pronunciation analysis
- **Google Text-to-Speech** for audio pronunciation
- **KoNLPy** for Korean natural language processing

## 📁 Project Structure

```
lyricspolyglot/
├── docker-compose.yml          # Main orchestration
├── frontend/                   # Next.js application
│   ├── pages/                  # Route-based pages
│   ├── components/             # Reusable UI components
│   ├── lib/                    # API hooks and utilities
│   ├── styles/                 # Global styles
│   └── public/                 # Static assets
├── backend/                    # FastAPI service
│   ├── app/
│   │   ├── api/                # Route handlers
│   │   ├── core/               # Configuration and utilities
│   │   ├── models/             # Database models
│   │   ├── services/           # Business logic
│   │   └── workers/            # Celery tasks
│   ├── alembic/                # Database migrations
│   └── requirements.txt        # Python dependencies
└── .github/workflows/          # CI/CD pipelines
```

## 🔧 Development

### Prerequisites
- Docker and Docker Compose
- Node.js 20+ (for local frontend development)
- Python 3.11+ (for local backend development)

### Local Development

```bash
# Start all services in development mode
docker compose up -d

# View logs
docker compose logs -f

# Run backend tests
docker compose exec backend pytest

# Run frontend linting
docker compose exec frontend npm run lint

# Create new database migration
docker compose exec backend alembic revision --autogenerate -m "description"

# Seed database with demo data
docker compose exec backend python app/core/seed.py
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/login` | User authentication |
| GET | `/api/songs/{id}` | Get song metadata |
| GET | `/api/songs/{id}/lyrics` | Get time-synced lyrics |
| GET | `/api/vocab/define` | Get word definitions |
| POST | `/api/recordings/score` | Score pronunciation |
| GET | `/api/flashcards/today` | Get today's flashcards |
| POST | `/api/flashcards/{id}/grade` | Grade flashcard response |

## 🚀 Deployment

### Frontend (Vercel)
```bash
# Deploy to Vercel
vercel --prod
```

### Backend (Render/Railway)
```bash
# Build and deploy backend
docker build -t lyricspolyglot-backend ./backend
```

## 🧪 Testing

```bash
# Backend tests
cd backend && pytest

# Frontend tests
cd frontend && npm test

# E2E tests (coming soon)
npm run test:e2e
```

## 📝 Environment Variables

### Backend (.env.dev)
```env
DATABASE_URL=postgresql+asyncpg://lyrics:lyrics@db:5432/lyrics_dev
REDIS_URL=redis://redis:6379
JWT_SECRET=your-secret-key
PROJECT_NAME=LyricsPolyglot
GOOGLE_APPLICATION_CREDENTIALS=/secrets/gcloud.json
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Roadmap

### Phase 1 (MVP) ✅
- [x] Basic song player with time-synced lyrics
- [x] User authentication
- [x] Vocabulary lookup
- [x] Basic pronunciation scoring

### Phase 2 🚧
- [ ] Social features and challenges
- [ ] Advanced analytics
- [ ] User progress tracking
- [ ] Community song submissions

### Phase 3 📅
- [ ] Additional languages (Japanese, Spanish)
- [ ] Mobile app
- [ ] Premium subscription features
- [ ] AI-powered song recommendations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- BTS for inspiring the demo content
- The Korean language learning community
- Open source contributors

---

**Happy Learning! 🎵🇰🇷**
