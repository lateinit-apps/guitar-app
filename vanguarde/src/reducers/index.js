import {createReducer, current} from '@reduxjs/toolkit';

const initialState = {
    songList: [],
    loading: false,
    error: null,
};

const songReducer = createReducer(
    initialState,
    {
        fetchBegin: (state, action) => {
            state.loading = true;
            state.error = null;
        },
        fetchSongListSuccess: (state, action) => {
            const songList = action.payload.songList;
            state.loading = false;
            state.songList = songList;
            console.log('new state: ', current(state));
        },
        fetchFailure: (state, action) => {
            state.loading = false;
            state.error = action.payload.error;
        },
    },
);

export default songReducer;
