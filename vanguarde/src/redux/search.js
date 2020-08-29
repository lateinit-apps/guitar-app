import {createSlice} from '@reduxjs/toolkit';

import AwesomeDebouncePromise from 'awesome-debounce-promise';

import {makeSongQuery} from './common';

const initialState = {
    searchBarIsVisible: false,
    searchQuery: null,
    artistQuery: null,
    releaseQuery: null,
    songQuery: null,
    genreQuery: null,
    sorting: null, // null, 'asc', 'desc'
};

const searchSlice = createSlice({
    name: 'searchBar',
    initialState,
    reducers: {
        toggleSearchBar(state, action) {
            console.log({state, action});
            state.searchBarIsVisible = !state.searchBarIsVisible;
        },
        changeSearchQuery(state, action) {
            console.log('changeSearchQuery', action.payload);
            state.searchQuery = action.payload;
        },
        toggleSorting: (state, action) => {
            state.sorting = state.sorting === 'asc' ? 'desc' : 'asc';
        },
        changeArtistQuery: (state, action) => {
            state.artistQuery = action.payload;
        },
        changeReleaseQuery: (state, action) => {
            state.releaseQuery = action.payload;
        },
        changeSongQuery: (state, action) => {
            state.songQuery = action.payload;
        },
        changeGenreQuery: (state, action) => {
            state.genreQuery = action.payload;
        },
    },
});

export const ARTIST_QUERY = 'ARTIST_QUERY';
export const RELEASE_QUERY = 'RELEASE_QUERY';
export const SONG_QUERY = 'SONG_QUERY';
export const GENRE_QUERY = 'GENRE_QUERY';

// eslint-disable-next-line new-cap
const makeSongQueryDebounced = AwesomeDebouncePromise(
    makeSongQuery,
    500,
);

export const killme = (eventType, value) => {
    return (dispatch, getState, {apiConfig}) => {
        switch (eventType) {
        case 'artists':
            dispatch(actions.changeArtistQuery(value));
            break;
        case 'songs':
            dispatch(actions.changeSongQuery(value));
            break;
        case 'releases':
            dispatch(actions.changeReleaseQuery(value));
            break;
        case 'genre':
            dispatch(actions.changeGenreQuery(value));
        };
        makeSongQueryDebounced(dispatch, getState, {apiConfig});
    };
};

export function handleSearchChange(event) {
    console.log('handleSearchChange:', event);
    const value = event.target.value;
    return (dispatch, getState, {apiConfig}) => {
        console.log('inside func');
        dispatch(changeSearchQuery(value));
        makeSongQueryDebounced(dispatch, getState, {apiConfig});
    };
}

export function handleSortToggle(event) {
    return (dispatch, getState, {apiConfig}) => {
        dispatch(toggleSorting());
        makeSongQuery(dispatch, getState, {apiConfig});
    };
}

export function handleArtistChange(event) {
    console.log('handleArtistChange', event);
    const value = event.target.value;
    return (dispatch, getState, {apiConfig}) => {
        dispatch(actions.changeArtistQuery(value));
        makeSongQuery(dispatch, getState, {apiConfig});
    };
}

export function handleSongChange(event) {
    const value = event.target.value;
    return (dispatch, getState, {apiConfig}) => {
        dispatch(actions.changeSongQuery(value));
        makeSongQuery(dispatch, getState, {apiConfig});
    };
}

export function handleToggleSearchBar(event) {
    return (dispatch) => {
        dispatch(toggleSearchBar);
    };
}

export const {actions, reducer} = searchSlice;
export const {toggleSearchBar, changeSearchQuery, toggleSorting} = actions;
export default reducer;
