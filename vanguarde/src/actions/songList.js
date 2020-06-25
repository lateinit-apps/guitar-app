import axios from 'axios';

import {FETCH_SONG_LIST_SUCCESS,
    TOGGLE_SEARCH_BAR} from '../constants/action-types';

import {fetchBegin, fetchError, handleError, handleSuccess} from './index';


export const fetchSongListSuccess = (songList) => ({
    type: FETCH_SONG_LIST_SUCCESS,
    payload: {songList},
});

export function getSongList() {
    return (dispatch, getState, {apiConfig}) => {
        console.log('getSongList');
        dispatch(fetchBegin());
        axios.get(`${apiConfig.url}/songs`)
            .then((res) => {
                console.log({res});
                dispatch(fetchSongListSuccess(res.data));
                dispatch(handleSuccess(res));
            })
            .catch((error) => {
                console.log('error');
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
