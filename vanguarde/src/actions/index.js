import {FETCH_BEGIN, FETCH_FAILURE} from '../constants/action-types';
import {store} from 'react-notifications-component';

export const fetchBegin = () => ({
    type: FETCH_BEGIN,
});

export const fetchError = (error) => ({
    type: FETCH_FAILURE,
    payload: {error},
});

export function handleSuccess(response) {
    return () => {
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
    };
}

export function handleError(errorObj) {
    console.log({errorObj});
    return (dispatch) => {
        store.addNotification({
            title: 'Error!',
            message: 'Check console log for more info',
            dismiss: {
                duration: 4000,
                onScreen: true,
            },
            type: 'success',
            insert: 'top',
            container: 'top-right',
            animationIn: ['animated', 'fadeIn'],
            animationOut: ['animated', 'fadeOut'],
        });
    };
}
