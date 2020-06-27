import {
    CHANGE_SEARCH_QUERY, TOGGLE_SEARCH_BAR,
} from '../constants/action-types';

const initialState = {
    searchBarToggle: false,
    searchQuery: '',
};

const searchReducer = (state = initialState, action) => {
    switch (action.type) {
    case TOGGLE_SEARCH_BAR:
        return {
            ...state,
            searchBarToggle: (!state.searchBarToggle),
        };
    case CHANGE_SEARCH_QUERY:
        return {
            ...state,
            searchQuery: action.payload.searchQuery,
        };
    default:
        return state;
    }
};


export default searchReducer;
