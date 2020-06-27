import {FETCH_BEGIN, FETCH_FAILURE} from '../constants/action-types';

export const fetchBegin = () => ({
    type: FETCH_BEGIN,
});

export const fetchError = (error) => ({
    type: FETCH_FAILURE,
    payload: {error},
});

export function handleSuccess(response) {
    return (dispatch) => {
    // TODO
    };
}

export function handleError(errorObj) {
    return (dispatch) => {
    // TODO
    };
}
