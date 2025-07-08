import React from 'react';
import Head from 'next/head';
import SongPlayer from '../components/SongPlayer';

const demoLyrics = [
  { word: "안녕하세요", start_ms: 0, end_ms: 2000 },
  { word: "반갑습니다", start_ms: 2000, end_ms: 4000 },
  { word: "오늘도", start_ms: 4000, end_ms: 5000 },
  { word: "좋은", start_ms: 5000, end_ms: 6000 },
  { word: "하루", start_ms: 6000, end_ms: 8000 },
  { word: "되세요", start_ms: 8000, end_ms: 10000 },
  { word: "감사합니다", start_ms: 10000, end_ms: 12000 },
  { word: "안녕히", start_ms: 12000, end_ms: 14000 },
  { word: "가세요", start_ms: 14000, end_ms: 16000 },
];

export default function Demo() {
  return (
    <>
      <Head>
        <title>Demo - LyricsPolyglot</title>
        <meta name="description" content="Demo of the LyricsPolyglot song player" />
      </Head>
      <main className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-8">
        <div className="container mx-auto px-4">
          <div className="text-center mb-8">
            <h1 className="text-4xl font-bold text-gray-900 mb-4">
              LyricsPolyglot Demo
            </h1>
            <p className="text-xl text-gray-600">
              Experience interactive Korean learning through music
            </p>
          </div>

          <SongPlayer songId={1} lyrics={demoLyrics} />

          <div className="mt-8 text-center">
            <a
              href="/"
              className="inline-block bg-gray-600 text-white px-6 py-3 rounded-lg hover:bg-gray-700 transition-colors"
            >
              Back to Home
            </a>
          </div>
        </div>
      </main>
    </>
  );
}