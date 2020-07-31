import {current, createSlice} from '@reduxjs/toolkit';

import {makeSongQuery} from './common';

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

export function getSongList(searchQuery = {}) {
    return (dispatch, getState, {apiConfig}) => {
        makeSongQuery(dispatch, getState, {apiConfig}, searchQuery);
    };
}

const {actions, reducer} = songSlice;
export const {fetchBegin, fetchSongListSuccess, fetchError, toggleSorting} = actions;
export default reducer;
