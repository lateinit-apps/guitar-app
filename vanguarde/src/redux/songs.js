import {current, createSlice} from '@reduxjs/toolkit';

import axios from 'axios';

import {handleError, handleSuccess} from './common';

const initialState = {
    songList: [],
    loading: false,
    error: null,
};

const songSlice = createSlice({
    name: 'songs',
    initialState,
    reducers: {
        fetchBegin: (state, action) => {
            state.loading = true;
            state.error = null;
        },
        fetchSongListSuccess: (state, action) => {
            const songList = action.payload;
            state.loading = false;
            state.songList = songList;
            console.log('new state: ', current(state));
        },
        fetchError: (state, action) => {
            state.loading = false;
            state.error = action.payload.error;
        },
    },
});

export function makeSongQuery(dispatch, getState, {apiConfig}, searchQuery = {}) {
    dispatch(fetchBegin());
    console.log({searchQuery});
    axios.get(`${apiConfig.url}/songs`, {params: searchQuery})
        .then((res) => {
            dispatch(fetchSongListSuccess(res.data));
            handleSuccess(res);
        })
        .catch((error) => {
            dispatch(fetchError(error));
            handleError(error);
        });
}

export function getSongList(searchQuery = {}) {
    return (dispatch, getState, {apiConfig}) => {
        makeSongQuery(dispatch, getState, {apiConfig}, searchQuery);
    };
}


const {actions, reducer} = songSlice;
export const {fetchBegin, fetchSongListSuccess, fetchError} = actions;
export default reducer;
