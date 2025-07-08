import React, { useEffect, useRef, useState } from 'react';
import WaveSurfer from 'wavesurfer.js';

interface LyricLine {
  word: string;
  start_ms: number;
  end_ms: number;
}

interface SongPlayerProps {
  songId: number;
  lyrics: LyricLine[];
}

const SongPlayer: React.FC<SongPlayerProps> = ({ songId, lyrics }) => {
  const waveformRef = useRef<HTMLDivElement>(null);
  const wavesurferRef = useRef<WaveSurfer | null>(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentTime, setCurrentTime] = useState(0);
  const [currentLyricIndex, setCurrentLyricIndex] = useState(0);

  useEffect(() => {
    if (waveformRef.current) {
      wavesurferRef.current = WaveSurfer.create({
        container: waveformRef.current,
        waveColor: '#4F46E5',
        progressColor: '#7C3AED',
        cursorColor: '#1F2937',
        barWidth: 2,
        barRadius: 3,
        cursorWidth: 1,
        height: 80,
        barGap: 3,
      });

      // Load audio file (placeholder)
      wavesurferRef.current.load('/audio/demo-song.mp3');

      wavesurferRef.current.on('audioprocess', (time) => {
        setCurrentTime(time * 1000); // Convert to milliseconds

        // Find current lyric
        const currentIndex = lyrics.findIndex(
          (lyric) => time * 1000 >= lyric.start_ms && time * 1000 <= lyric.end_ms
        );
        if (currentIndex !== -1 && currentIndex !== currentLyricIndex) {
          setCurrentLyricIndex(currentIndex);
        }
      });

      wavesurferRef.current.on('play', () => setIsPlaying(true));
      wavesurferRef.current.on('pause', () => setIsPlaying(false));
    }

    return () => {
      if (wavesurferRef.current) {
        wavesurferRef.current.destroy();
      }
    };
  }, [lyrics]);

  const togglePlay = () => {
    if (wavesurferRef.current) {
      wavesurferRef.current.playPause();
    }
  };

  return (
    <div className="max-w-4xl mx-auto p-6 bg-white rounded-lg shadow-lg">
      <div className="mb-6">
        <h2 className="text-2xl font-bold text-gray-900 mb-2">Song Player</h2>
        <p className="text-gray-600">Song ID: {songId}</p>
      </div>

      {/* Waveform */}
      <div className="mb-6">
        <div ref={waveformRef} className="w-full" />
        <div className="flex justify-center mt-4">
          <button
            onClick={togglePlay}
            className="bg-primary-600 text-white px-6 py-2 rounded-lg hover:bg-primary-700 transition-colors"
          >
            {isPlaying ? 'Pause' : 'Play'}
          </button>
        </div>
      </div>

      {/* Lyrics Display */}
      <div className="space-y-2">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">Lyrics</h3>
        {lyrics.map((lyric, index) => (
          <div
            key={index}
            className={`p-3 rounded-lg transition-colors ${
              index === currentLyricIndex
                ? 'bg-primary-100 border-l-4 border-primary-600'
                : 'bg-gray-50'
            }`}
          >
            <span className="text-lg font-medium">{lyric.word}</span>
            <div className="text-sm text-gray-500 mt-1">
              {Math.floor(lyric.start_ms / 1000)}s - {Math.floor(lyric.end_ms / 1000)}s
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default SongPlayer;