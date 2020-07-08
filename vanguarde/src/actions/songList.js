import axios from 'axios';

import {fetchBegin, fetchError, handleError, handleSuccess} from './fetching';

import AwesomeDebouncePromise from 'awesome-debounce-promise';

import {createAction} from '@reduxjs/toolkit';


export const fetchSongListSuccess = createAction('fetch/songList/success');

export const toggleSearchBar = createAction('search_bar/toggle');

export const changeSearchQuery = createAction('search_bar/change_query');

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

export function handleSearchChange(event) {
    const value = event.target.value;
    return (dispatch, getState, {apiConfig}) => {
        dispatch(changeSearchQuery(value));
        makeSongQueryDebounced(dispatch, getState,
            {apiConfig},
            {'name': value},
        );
    };
}
