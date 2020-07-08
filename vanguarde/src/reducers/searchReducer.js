import {createSlice} from '@reduxjs/toolkit';

import AwesomeDebouncePromise from 'awesome-debounce-promise';

import {makeSongQuery} from './songReducer';

const initialState = {
    searchBarIsVisible: false,
    searchQuery: '',
};

const searchSlice = createSlice({
    name: 'searchBar',
    initialState,
    reducers: {
        toggleSearchBar(state, action) {
            state.searchBarIsVisible = !state.searchBarIsVisible;
        },
        changeSearchQuery(state, action) {
            state.searchQuery = action.payload;
        },
    },
});

// eslint-disable-next-line new-cap
const makeSongQueryDebounced = AwesomeDebouncePromise(
    makeSongQuery,
    500,
);

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

const {actions, reducer} = searchSlice;
export const {toggleSearchBar, changeSearchQuery} = actions;
export default reducer;
