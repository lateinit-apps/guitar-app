import React from 'react';
import {BrowserRouter as Router} from 'react-router-dom';

import '@fortawesome/fontawesome-free/css/all.min.css';
import 'bootstrap-css-only/css/bootstrap.min.css';
import 'mdbreact/dist/css/mdb.css';
import MainPage from "./components/MainPage";
import {Footer} from "./components/Footer";
import {Header} from "./components/Header";


/**
 * @return {boolean}
 */
function App() {
    return (
        <Router>
            <Header/>
            <MainPage/>
            <Footer/>
        </Router>

    );
}

export default App;
