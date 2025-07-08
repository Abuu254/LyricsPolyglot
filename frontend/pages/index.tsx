import Head from 'next/head';
import Link from 'next/link';

export default function Home() {
  return (
    <>
      <Head>
        <title>LyricsPolyglot - Learn Korean Through Music</title>
        <meta name="description" content="Learn Korean through interactive song lyrics" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
        <div className="container mx-auto px-4 py-16">
          <div className="text-center">
            <h1 className="text-6xl font-bold text-gray-900 mb-6">
              LyricsPolyglot
            </h1>
            <p className="text-xl text-gray-600 mb-8">
              Learn Korean through interactive, time-synced song lyrics
            </p>
            <div className="space-x-4">
              <Link href="/demo">
                <button className="bg-primary-600 text-white px-8 py-3 rounded-lg hover:bg-primary-700 transition-colors">
                  Try Demo
                </button>
              </Link>
              <button className="border border-gray-300 text-gray-700 px-8 py-3 rounded-lg hover:bg-gray-50 transition-colors">
                Learn More
              </button>
            </div>
          </div>

          {/* Features Section */}
          <div className="mt-16 grid md:grid-cols-3 gap-8">
            <div className="text-center p-6 bg-white rounded-lg shadow-md">
              <div className="text-4xl mb-4">🎵</div>
              <h3 className="text-xl font-semibold mb-2">Time-Synced Lyrics</h3>
              <p className="text-gray-600">Lyrics highlight in real-time as the song plays</p>
            </div>
            <div className="text-center p-6 bg-white rounded-lg shadow-md">
              <div className="text-4xl mb-4">🎤</div>
              <h3 className="text-xl font-semibold mb-2">Pronunciation Scoring</h3>
              <p className="text-gray-600">AI-powered feedback on Korean pronunciation</p>
            </div>
            <div className="text-center p-6 bg-white rounded-lg shadow-md">
              <div className="text-4xl mb-4">📚</div>
              <h3 className="text-xl font-semibold mb-2">Spaced Repetition</h3>
              <p className="text-gray-600">Smart flashcards for vocabulary retention</p>
            </div>
          </div>
        </div>
      </main>
    </>
  );
}