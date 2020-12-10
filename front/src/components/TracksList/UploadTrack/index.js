import IconButton from '@material-ui/core/IconButton';
import InputBase from '@material-ui/core/InputBase';
import Paper from '@material-ui/core/Paper';
import BackupIcon from '@material-ui/icons/Backup';
import React, { useState, useRef } from 'react';
import { uploadTrack } from '../../../services/tracks.service';
import DialogTitle from '@material-ui/core/DialogTitle';
import Dialog from '@material-ui/core/Dialog';
import DialogContent from '@material-ui/core/DialogContent';
import DialogActions from '@material-ui/core/DialogActions';
import Button from '@material-ui/core/Button';
import Alert from '@material-ui/lab/Alert';
import Collapse from '@material-ui/core/Collapse';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';

const UploadTrack = ({ open, onCloseDialog = () => { } }) => {
    const fileRef = useRef(null);
    const [file, setFile] = useState(null);
    const [fileName, setFileName] = useState('');
    const [showAlert, setShowAlert] = useState(false);

    const handleChangeFile = (event) => {
        const fileSelected = event.target.files[0];
        console.log(fileSelected);
        if (fileSelected) {
            setFile(fileSelected);
        }
    }

    const sendFile = () => {
        if (file && fileName) {
            uploadTrack(file, fileName)
                .then(result => { onCloseDialog(true); })
                .catch(err => { console.log(err) })
        } else {
            setShowAlert(true);
        }
    }


    const handleClickSelectFile = () => {
        fileRef.current.click();
    };

    const handleClose = () => {
        onCloseDialog();
    };

    return (
        <Dialog onClose={handleClose} open={open}>
            <DialogTitle id="simple-dialog-title">Enviar música</DialogTitle>
            <DialogContent>
            
                <Grid container style={{marginBottom: 10}}>
                    <Grid item xs={12}>
                        <Collapse in={showAlert}>
                            <Alert variant="outlined" severity="error" onClose={() => setShowAlert(false)}>Nome e arquivo são obrigatórios</Alert>
                        </Collapse>
                    </Grid>
                </Grid>


                <Grid container justify="center" alignItems="center"
                
                >
                    <Grid item xs={6}>

                    <TextField label="Nome da música" size="small" variant="outlined"  onChange={(event) => setFileName(event.target.value)} />                      
                    <input ref={fileRef} type="file" style={{ display: 'none' }} accept="audio/mp3" onChange={handleChangeFile} />
                    </Grid>
                    <Grid item xs={6} justify="center">
                        <Button
                        style={{ margin: '0 4px', width: '100%'}}                            
                            onClick={handleClickSelectFile}                            
                            color={"primary"}
                            variant={file ?"contained" :"outlined"}
                            startIcon={<BackupIcon />}
                            >{file ? 'Trocar Arquivo': 'Selecionar Arquivo'}</Button>

                    </Grid>
                </Grid>            
            </DialogContent>
            <DialogActions>
                <Button onClick={handleClose} color="primary">Voltar</Button>
                <Button onClick={sendFile} color="primary">Enviar</Button>
            </DialogActions>
        </Dialog>

    )

}


export default UploadTrack;