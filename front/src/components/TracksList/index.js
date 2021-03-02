import List from '@material-ui/core/List';
import Pagination from '@material-ui/lab/Pagination';
import React, { useEffect, useState } from 'react';
import { getAllTracks } from "../../services/tracks.service";
import Search from '../Search';
import Container from '@material-ui/core/Container';
import TrackItem from './TrackItem';
import UploadTrack from './UploadTrack';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import IconButton from '@material-ui/core/IconButton';
import BackupIcon from '@material-ui/icons/Backup';
import Snackbar from '@material-ui/core/Snackbar';
import Alert from '@material-ui/lab/Alert';

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

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
        padding: 30,
        paddingTop: 100,
    },
    paper: {
        padding: theme.spacing(2),
        textAlign: 'center',
        color: theme.palette.text.secondary,
    },
}));

const TracksList = () => {
    const classes = useStyles();

    const [paginateResult, setPaginateResult] = useState(paginateInit);
    const [idTrackPlaying, setIdTrackPlaying] = useState(null);
    const [filter, setFilter] = useState('');
    const [openUploadDialog, setOpenUploadDialog] = useState(false);
    const [openSnackSuccesAdded, setOpenSnackSuccesAdded] = useState(false);

    const getList = async (page = 1, search = '') => {
        try {
            const result = await getAllTracks(page, search);
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

    const handleChangePage = (event, value) => {
        if (filter) {
            getList(value, filter);
        } else {
            getList(value)
        }
    };

    const handleChangePlay = (change) => {
        console.log(change);
        if (change && change.isPlay) {
            setIdTrackPlaying(change.trackId);
        }
    }

    const trackIsPlay = (idTrack) => {
        if (idTrackPlaying) {
            return idTrackPlaying == idTrack;
        }
        return false;
    }

    const handleChangeText = (value) => {
        getList(1, value);
        setFilter(value);
    }

    const handleCloseDialog = (isAddedTrack) => {
        if (isAddedTrack) {
            getList();
            setOpenSnackSuccesAdded(true);
        }

        setOpenUploadDialog(false);
    }



    return (

        <div className={classes.root}>
            <Container fixed>

                <Grid container justify="center" spacing={3}>
                    <Grid item>
                        <Search onChangeText={handleChangeText} />
                    </Grid>
                    <Grid item>

                        <IconButton aria-label="enviar" onClick={() => setOpenUploadDialog(true)}>
                            <BackupIcon />
                        </IconButton>
                        <UploadTrack open={openUploadDialog} onCloseDialog={handleCloseDialog} />
                    </Grid>

                </Grid>
                <Grid container justify="center" spacing={3}>
                    <Grid item>
                        <List>
                            {paginateResult?.result?.map(track =>
                                (<TrackItem
                                    key={track.id}
                                    track={track}
                                    isPlay={() => trackIsPlay(track.id)}
                                    onChangePlay={handleChangePlay} />)
                            )}
                        </List>
                    </Grid>
                </Grid>
                <Grid container justify="center" spacing={3}>
                    <Grid item>
                        <Pagination count={paginateResult.paginate.pages} page={paginateResult.paginate.page} onChange={handleChangePage} />
                    </Grid>
                </Grid>
            </Container>
            <Snackbar open={openSnackSuccesAdded} autoHideDuration={6000} onClose={()=> setOpenSnackSuccesAdded(false)}>
                <Alert onClose={() => setOpenSnackSuccesAdded(false)} severity="success">
                    Música adicionada com sucesso
                </Alert>
            </Snackbar>
        </div>

    );
}

export default TracksList;