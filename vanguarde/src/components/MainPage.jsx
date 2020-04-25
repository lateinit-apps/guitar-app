import React, { Component } from "react";
import {SongCard} from "./SongCard.jsx";
import {MDBBtn, MDBCard, MDBCardBody, MDBCol, MDBContainer, MDBIcon, MDBInput, MDBRow} from "mdbreact";
import placeholder from "../assets/150.png";
import {SearchOptions} from "./SearchOptions";


class MainPage extends Component {

    constructor(props) {
        super(props);
        this.state = {
            searchOptionsToggle: false
        }

        this.handleSearchOptionClick = this.handleSearchOptionClick.bind(this);
    }

    handleSearchOptionClick(e) {
        this.setState(state => ({
            searchOptionsToggle: !state.searchOptionsToggle
        }))
    }

    render() {
        return (

            <MDBContainer fluid>
                <MDBRow>
                    <MDBCol md={2}>

                    </MDBCol>
                    <MDBCol md={8}>
                        <MDBRow className={"d-flex flex-row"}>
                            <MDBCol md="10">
                                <MDBInput label="Search"/>
                            </MDBCol>
                            <MDBCol  md="2"><MDBBtn floating size="lg" color="elegant" onClick={this.handleSearchOptionClick}>
                                <MDBIcon icon="tools" size="2x"/>
                            </MDBBtn></MDBCol>
                        </MDBRow>
                        {this.state.searchOptionsToggle ?
                            <SearchOptions/>
                        : null}
                        <SongCard artist={"Some cool dude"} trackName={"Some cool track"}/>
                        <SongCard artist={"Взрвыв кабачка в коляске с поносом"} trackName={"Мрачный аборт в сарае"}/>
                    </MDBCol>
                    <MDBCol md={2}>
                    </MDBCol>
                </MDBRow>
            </MDBContainer>


        );

    }

}

export default MainPage;
