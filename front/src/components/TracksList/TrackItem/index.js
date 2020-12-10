import React, { useState, useEffect } from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemAvatar from '@material-ui/core/ListItemAvatar';
import Avatar from '@material-ui/core/Avatar';
import PlayArrowIcon from '@material-ui/icons/PlayArrow';
import PauseIcon from '@material-ui/icons/Pause';
import ListItemText from '@material-ui/core/ListItemText';
import Player from '../../Player';


const TrackItem = ({ track, isPlay,  onChangePlay = () => {} }) => {
    const [isPlaying, setIsPlaying] = useState(false);

    useEffect(() => {
        setIsPlaying(isPlay);
    }, [isPlay]);

    const togglePlay = () => {
        const togglePlay = !isPlaying;
        setIsPlaying(togglePlay);
        
        onChangePlay({
            isPlay: togglePlay,
            trackId: track.id
        });
    }

    return (
        <>
            <ListItem>
                <ListItemAvatar>
                    <Avatar onClick={togglePlay}>
                        {isPlaying ? <PauseIcon /> : <PlayArrowIcon />}
                    </Avatar>
                </ListItemAvatar>
                <ListItemText primary={track.name} secondary={`${track.filename} - ${track.size}kb`} />
            </ListItem>
            <Player audioId={track.id} isPlaying={isPlaying} />
        </>
    )
}


export default TrackItem;