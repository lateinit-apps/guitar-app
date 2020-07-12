import {store} from 'react-notifications-component';

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
