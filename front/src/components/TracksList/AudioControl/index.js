import React, { useRef, useEffect } from 'react';

const AudioControl = ({ audioId, isPlaying = false }) => {
    const playerRef = useRef(null);

    useEffect(() => {
        if (isPlaying) {
            playerRef.current.play();
        } else {
            playerRef.current.pause();
        }

    }, [isPlaying]);

    return (
        <audio ref={playerRef} controls style={{ display: 'none' }} >
            <source src={`http://localhost:5000/tracks/play/${audioId}`} type="audio/mp3" />
        </audio>
    )
}

export default AudioControl;