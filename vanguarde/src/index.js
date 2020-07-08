import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

import {Provider} from 'react-redux';
import {configureStore, getDefaultMiddleware} from '@reduxjs/toolkit';
import songReducer from './reducers/songReducer';
import searchReducer from './reducers/searchReducer';
import thunk from 'redux-thunk';

import ReactNotification from 'react-notifications-component';
import 'react-notifications-component/dist/theme.css';

const config = {
    apiConfig: {
        url: 'http://127.0.0.1:5000/',
    },
};

const rootReducer = {
    searchReducer: searchReducer,
    songReducer: songReducer,
};
const store = configureStore({
    reducer: rootReducer,
    middleware: [thunk.withExtraArgument(config), ...getDefaultMiddleware()],
    devTools: true, // TODO: disable in production
});

ReactDOM.render(
    <Provider store={store}>
        <ReactNotification />
        <App />
    </Provider>,
    document.getElementById('root'),
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
