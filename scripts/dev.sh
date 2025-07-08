#!/bin/bash

# LyricsPolyglot Development Script

echo "🎵 LyricsPolyglot Development Helper"
echo "====================================="

case "$1" in
  "start")
    echo "🚀 Starting all services..."
    docker compose up --build -d
    echo "✅ Services started!"
    echo "📱 Frontend: http://localhost:3000"
    echo "🔧 API Docs: http://localhost:8000/docs"
    ;;
  "stop")
    echo "🛑 Stopping all services..."
    docker compose down
    echo "✅ Services stopped!"
    ;;
  "logs")
    echo "📋 Showing logs..."
    docker compose logs -f
    ;;
  "test")
    echo "🧪 Running tests..."
    docker compose exec backend pytest
    ;;
  "lint")
    echo "🔍 Running linting..."
    docker compose exec frontend npm run lint
    ;;
  "seed")
    echo "🌱 Seeding database..."
    docker compose exec backend python app/core/seed.py
    ;;
  "migrate")
    echo "🗄️ Running migrations..."
    docker compose exec backend alembic upgrade head
    ;;
  "shell")
    echo "🐚 Opening backend shell..."
    docker compose exec backend python
    ;;
  *)
    echo "Usage: $0 {start|stop|logs|test|lint|seed|migrate|shell}"
    echo ""
    echo "Commands:"
    echo "  start   - Start all services"
    echo "  stop    - Stop all services"
    echo "  logs    - Show service logs"
    echo "  test    - Run backend tests"
    echo "  lint    - Run frontend linting"
    echo "  seed    - Seed database with demo data"
    echo "  migrate - Run database migrations"
    echo "  shell   - Open Python shell in backend"
    exit 1
    ;;
esac