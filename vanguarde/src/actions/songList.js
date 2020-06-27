import axios from 'axios';

import {FETCH_SONG_LIST_SUCCESS,
    TOGGLE_SEARCH_BAR, CHANGE_SEARCH_QUERY} from '../constants/action-types';

import {fetchBegin, fetchError, handleError, handleSuccess} from './index';


export const fetchSongListSuccess = (songList) => ({
    type: FETCH_SONG_LIST_SUCCESS,
    payload: {songList},
});

export function getSongList(searchQuery = {}) {
    return (dispatch, getState, {apiConfig}) => {
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
    };
}

export function toggleSearchBar() {
    return (dispatch, getState) => {
        dispatch(
            {type: TOGGLE_SEARCH_BAR},
        );
    };
}

export function changeSearchInput(event) {
    return (dispatch, getState) => {
        dispatch(
            {
                type: CHANGE_SEARCH_QUERY,
                payload: event.target.value,
            },
        );
    };
}
