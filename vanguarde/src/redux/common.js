import {store} from 'react-notifications-component';
import {fetchBegin, fetchError, fetchSongListSuccess} from './songs';
import axios from 'axios';

export function handleSuccess(response) {
    store.addNotification({
        title: 'Success!',
        message: 'Song list loaded',
        dismiss: {
            duration: 2000,
            onScreen: true,
        },
        type: 'success',
        insert: 'top',
        container: 'top-right',
        animationIn: ['animated', 'fadeIn'],
        animationOut: ['animated', 'fadeOut'],
    });
}

export function handleError(errorObj) {
    console.log({errorObj});
    store.addNotification({
        title: 'Error!',
        message: 'Check console log for more info',
        dismiss: {
            duration: 4000,
            onScreen: true,
        },
        type: 'danger',
        insert: 'top',
        container: 'top-right',
        animationIn: ['animated', 'fadeIn'],
        animationOut: ['animated', 'fadeOut'],
    });
}

export function makeSongQuery(dispatch, getState, {apiConfig}, searchQuery = {}) {
    dispatch(fetchBegin());
    console.log({searchQuery});
    const searchState = getState().searchReducer;
    const searchParams = {
        'name': searchState.searchQuery ? searchState.searchQuery : null,
        'sort_by': searchState.sorting ? 'name|' + searchState.sorting : null,
    };
    axios.get(`${apiConfig.url}songs`, {params: searchParams})
        .then((res) => {
            dispatch(fetchSongListSuccess(res.data));
            handleSuccess(res);
        })
        .catch((error) => {
            dispatch(fetchError(error));
            handleError(error);
        });
}
