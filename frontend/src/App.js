import React from 'react';
// import MainPage from "./components/MainPage";
import {
    MDBNavbar, MDBNavbarBrand, MDBNavbarNav, MDBNavItem, MDBNavLink, MDBNavbarToggler, MDBCollapse, MDBFormInline,
    MDBDropdown, MDBDropdownToggle, MDBDropdownMenu, MDBDropdownItem, MDBCol, MDBContainer, MDBRow, MDBFooter, MDBInput,
    MDBIcon, MDBCard, MDBCardBody, MDBBtn
} from "mdbreact";
import {BrowserRouter as Router} from 'react-router-dom';
import {InputGroup, FormControl} from "react-bootstrap";
import placeholder from '../public/150.png';

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
