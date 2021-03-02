import IconButton from '@material-ui/core/IconButton';
import InputBase from '@material-ui/core/InputBase';
import Paper from '@material-ui/core/Paper';
import { makeStyles } from '@material-ui/core/styles';
import SearchIcon from '@material-ui/icons/Search';
import React, { useState } from 'react';

const useStyles = makeStyles((theme) => ({
    root: {
        padding: '2px 4px',
        display: 'flex',
        alignItems: 'center'
    },
    input: {
        marginLeft: theme.spacing(1),
        flex: 1,
    },
    iconButton: {
        padding: 10,
    },
}));

const Search = ({ onChangeText = () => { } }) => {
    const classes = useStyles();
    const [text, setText] = useState('');

    const handleChangeText = (event) => {
        const value = event.target.value;
        setText(value);
        onChangeText(value);
    }

    const handleSubmit = (event) => {
        event.preventDefault();
        onChangeText(text);
    }

    return (
        <Paper component="form" className={classes.root} onSubmit={handleSubmit}>
            <InputBase
                className={classes.input}
                placeholder="Pesquisar Musicas"
                value={text} onChange={handleChangeText}
            />
            <IconButton type="submit" className={classes.iconButton} aria-label="search">
                <SearchIcon />
            </IconButton>

        </Paper>
    )
}

export default Search;