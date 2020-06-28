import {
    FETCH_BEGIN,
    FETCH_SONG_LIST_SUCCESS,
    FETCH_SONG_SUCCESS,
    FETCH_FAILURE,
} from '../constants/action-types';

const initialState = {
    songList: [],
    loading: false,
    error: null,
};

const songReducer = (state = initialState, action) => {
    switch (action.type) {
    case FETCH_BEGIN:
        return {
            ...state,
            loading: true,
            error: null,
        };
    case FETCH_SONG_LIST_SUCCESS:
        return {
            ...state,
            loading: false,
            songList: action.payload.songList,
        };
    case FETCH_SONG_SUCCESS:
        return {
            ...state,
            loading: false,
        };
    case FETCH_FAILURE:
        return {
            ...state,
            loading: false,
            error: action.payload.error,
        };
    default:
        return state;
    }
};


export default songReducer;
