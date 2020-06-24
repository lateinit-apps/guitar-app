import {
    CHANGE_SEARCH_QUERY, TOGGLE_SEARCH_BAR,
} from '../constants/action-types';

const initialState = {
    search_bar_toggle: false,
    search_query: '',
};

const searchReducer = (state = initialState, action) => {
    switch (action.type) {
    case TOGGLE_SEARCH_BAR:
        return {
            ...state,
            search_bar_toggle: (!state.search_bar_toggle),
        };
    case CHANGE_SEARCH_QUERY:
        return {
            ...state,
            search_query: action.payload.search_query,
        };
    default:
        return state;
    }
};


export default searchReducer;
