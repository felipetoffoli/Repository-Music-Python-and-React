import React, { useState, useEffect } from 'react';
import { Container } from './styles';
import { getAllTracks } from "../../services/tracks.service";
import List from '@material-ui/core/List';
import TrackItem from './TrackItem';
import Pagination from '@material-ui/lab/Pagination';

const paginateInit = {
    paginate: {
        limit: 10,
        page: 1,
        pages: 1,
        prev_num: null,
        total: 5
    },
    result: []
}

const TracksList = () => {
    const [paginateResult, setPaginateResult] = useState(paginateInit);
    const [idTrackPlaying, setIdTrackPlaying] = useState(null);

    const getList = async (page = 1) => {
        try {
            const result = await getAllTracks(page);
            const { data } = result;
            console.log(data);
            setPaginateResult(data);
        } catch (err) {
            console.log(err);
        }
    }

    useEffect(() => {
        getList();
    }, []);

    const handleChange = (event, value) => {
        getList(value);
    };

    const handleChangePlay = (change) => {
        console.log(change);
        if(change && change.isPlay){
            setIdTrackPlaying(change.trackId);
        }
    }

    const trackIsPlay = (idTrack) => {
        if (idTrackPlaying) {
            return idTrackPlaying == idTrack;
        }

        return false;
    }

    return (
        <Container>
            <List>
                {paginateResult?.result?.map(track =>
                    (<TrackItem
                        key={track.id}
                        track={track}
                        isPlay={() => trackIsPlay(track.id)}
                        onChangePlay={handleChangePlay} />)
                )}
            </List>
            <Pagination count={paginateResult.paginate.pages} page={paginateResult.paginate.page} onChange={handleChange} />
        </Container>
    );
}

export default TracksList;