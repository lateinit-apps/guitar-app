import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

import {Provider} from 'react-redux';
import {applyMiddleware, createStore, combineReducers} from 'redux';
import songReducer from './reducers';
import searchReducer from './reducers/searchReducer';
import thunk from 'redux-thunk';

const config = {
    apiConfig: {
        url: 'http://127.0.0.1:5000/',
    },
};

const store = createStore(
    combineReducers(
        {songReducer, searchReducer},
    ),
    applyMiddleware(thunk.withExtraArgument(config)),
);

ReactDOM.render(
    <Provider store={store}>
        <App />
    </Provider>,
    document.getElementById('root'),
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
