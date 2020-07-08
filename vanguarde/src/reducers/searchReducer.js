import {createReducer} from '@reduxjs/toolkit';

const initialState = {
    searchBarIsVisible: false,
    searchQuery: '',
};

const searchReducer = createReducer(
    initialState,
    {
        toggleSearchBar: (state, action) => {
            state.searchBarIsVisible = !state.searchBarIsVisible;
        },
        changeSearchQuery: (state, action) => {
            state.searchQuery = action.payload;
        },
    },
);

export default searchReducer;
