import axios from 'axios';

import {FETCH_SONG_LIST_SUCCESS,
    TOGGLE_SEARCH_BAR, CHANGE_SEARCH_QUERY} from '../constants/action-types';

import {fetchBegin, fetchError, handleError, handleSuccess} from './index';


export const fetchSongListSuccess = (songList) => ({
    type: FETCH_SONG_LIST_SUCCESS,
    payload: {songList},
});

function makeSongQuery(dispatch, getState, {apiConfig}, searchQuery = {}) {
    dispatch(fetchBegin());
    axios.get(`${apiConfig.url}/songs`, searchQuery)
        .then((res) => {
            dispatch(fetchSongListSuccess(res.data));
            dispatch(handleSuccess(res));
        })
        .catch((error) => {
            dispatch(fetchError(error));
            dispatch(handleError(error));
        });
}

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

export function changeSearchInput(event) {
    return {
        type: CHANGE_SEARCH_QUERY,
        payload: event.target.value,
    };
}

export function handleSearchChange(event) {
    return (dispatch, getState, {apiConfig}) => {
        dispatch(changeSearchInput(event));
        makeSongQuery(dispatch, getState, {apiConfig}, {'name': event.target.value});
    };
}
