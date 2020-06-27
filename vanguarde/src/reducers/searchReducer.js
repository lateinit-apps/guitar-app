import {
    CHANGE_SEARCH_QUERY, TOGGLE_SEARCH_BAR,
} from '../constants/action-types';

const initialState = {
    searchBarIsVisible: false,
    searchQuery: '',
};

const searchReducer = (state = initialState, action) => {
    switch (action.type) {
    case TOGGLE_SEARCH_BAR:
        return {
            ...state,
            searchBarIsVisible: (!state.searchBarIsVisible),
        };
    case CHANGE_SEARCH_QUERY:
        return {
            ...state,
            searchQuery: action.payload,
        };
    default:
        return state;
    }
};


export default searchReducer;
