import {createSlice} from '@reduxjs/toolkit';

import AwesomeDebouncePromise from 'awesome-debounce-promise';

import {makeSongQuery} from './common';

const initialState = {
    searchBarIsVisible: false,
    ominbarQuery: null,
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
        changeOmnibarQuery(state, action) {
            state.ominbarQuery = action.payload;
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

export const changeSearchQuery = (eventType, value) => {
    return (dispatch, getState, {apiConfig}) => {
        switch (eventType) {
        case ARTIST_QUERY:
            dispatch(actions.changeArtistQuery(value));
            break;
        case SONG_QUERY:
            dispatch(actions.changeSongQuery(value));
            break;
        case RELEASE_QUERY:
            dispatch(actions.changeReleaseQuery(value));
            break;
        case GENRE_QUERY:
            dispatch(actions.changeGenreQuery(value));
            break;
        default:
            console.log('Wrong eventType ', {eventType});
        };
        makeSongQueryDebounced(dispatch, getState, {apiConfig});
    };
};

export function handleOmnibarChange(event) {
    const value = event.target.value;
    return (dispatch, getState, {apiConfig}) => {
        dispatch(actions.changeSongQuery(value));
        makeSongQueryDebounced(dispatch, getState, {apiConfig});
    };
}

export function handleSortToggle(event) {
    return (dispatch, getState, {apiConfig}) => {
        dispatch(toggleSorting());
        makeSongQuery(dispatch, getState, {apiConfig});
    };
}

export function handleToggleSearchBar(event) {
    return (dispatch) => {
        dispatch(toggleSearchBar);
    };
}

export const {actions, reducer} = searchSlice;
export const {toggleSearchBar, changeOmnibarhQuery, toggleSorting} = actions;
export default reducer;
