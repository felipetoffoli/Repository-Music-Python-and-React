import React, { useRef, useEffect} from 'react';
import {Audio} from './styles'

const Player = ({audioId, isPlaying}) => {
    const playerRef = useRef(null);

    useEffect(() => {
        if(isPlaying){
            playerRef.current.play();
        } else {
            playerRef.current.pause();
        }
        
    }, [isPlaying]);

    return (
        <Audio ref={playerRef} controls >
           <source src={`http://localhost:5000/tracks/play/${audioId}`} type="audio/mp3"/>
        </Audio>
    )
}

export default Player;