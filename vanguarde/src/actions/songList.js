import axios from 'axios';

import {FETCH_SONG_LIST_SUCCESS,
    TOGGLE_SEARCH_BAR, CHANGE_SEARCH_QUERY} from '../constants/action-types';

import {fetchBegin, fetchError, handleError, handleSuccess} from './index';

import AwesomeDebouncePromise from 'awesome-debounce-promise';


export const fetchSongListSuccess = (songList) => ({
    type: FETCH_SONG_LIST_SUCCESS,
    payload: {songList},
});

function makeSongQuery(dispatch, getState, {apiConfig}, searchQuery = {}) {
    dispatch(fetchBegin());
    console.log({searchQuery});
    axios.get(`${apiConfig.url}/songs`, {params: searchQuery})
        .then((res) => {
            dispatch(fetchSongListSuccess(res.data));
            dispatch(handleSuccess(res));
        })
        .catch((error) => {
            dispatch(fetchError(error));
            dispatch(handleError(error));
        });
}

// eslint-disable-next-line new-cap
const makeSongQueryDebounced = AwesomeDebouncePromise(
    makeSongQuery,
    500,
);

export function getSongList(searchQuery = {}) {
    return (dispatch, getState, {apiConfig}) => {
        makeSongQuery(dispatch, getState, {apiConfig}, searchQuery);
    };
}

export function toggleSearchBar() {
    return {
        type: TOGGLE_SEARCH_BAR,
    };
}

export function changeSearchInput(value) {
    return {
        type: CHANGE_SEARCH_QUERY,
        payload: value,
    };
}

export function handleSearchChange(event) {
    const value = event.target.value;
    return (dispatch, getState, {apiConfig}) => {
        dispatch(changeSearchInput(value));
        makeSongQueryDebounced(dispatch, getState,
            {apiConfig},
            {'name': value},
        );
    };
}
