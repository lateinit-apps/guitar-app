import {createSlice} from '@reduxjs/toolkit';

import AwesomeDebouncePromise from 'awesome-debounce-promise';

import {makeSongQuery} from './songs';

const initialState = {
    searchBarIsVisible: false,
    searchQuery: '',
    sorting: null, // null, 'asc', 'desc'
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
        toggleSorting: (state, action) => {
            state.sorting = state.sorting === 'asc' ? 'desc' : 'asc';
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

export function handleSortToggle(event) {
    return (dispatch, getState, {apiConfig}) => {
        dispatch(toggleSorting());
        const searchState = getState().searchReducer;
        makeSongQuery(dispatch, getState,
            {apiConfig}, {'name': searchState.searchQuery, 'sort_by': 'name|'+searchState.sorting});
    };
    // dispatch(actions[toggleSearchBar]);
}

const {actions, reducer} = searchSlice;
export const {toggleSearchBar, changeSearchQuery, toggleSorting} = actions;
export default reducer;
