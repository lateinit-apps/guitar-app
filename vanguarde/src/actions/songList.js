import axios from "axios";

import { FETCH_SONG_LIST_SUCCESS } from "../constants/action-types";

import { fetchBegin, fetchError, handleError } from "./index";


export const fetchSongListSuccess = songList => ({
    type: FETCH_SONG_LIST_SUCCESS,
    payload: { songList }
});

export function getSongList() { return (dispatch, getState, { apiConfig }) => {
    console.log('getSongList');
    dispatch(fetchBegin());
    axios.get(`http://127.0.0.1:5000/songs`) // FIXME: hardcoded API
        .then(res => {
            console.log({res});
            dispatch(fetchSongListSuccess(res.data));
            // dispatch(handleSuccess(res))
        })
        .catch(error => {
            console.log("error");
            dispatch(fetchError(error));
            dispatch(handleError(error));
        })
};}