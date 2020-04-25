import React, { Component } from "react";
import {SongCard} from "./SongCard.jsx";
import {MDBBtn, MDBCard, MDBCardBody, MDBCol, MDBContainer, MDBIcon, MDBInput, MDBRow} from "mdbreact";
import placeholder from "../assets/150.png";


class MainPage extends Component {

    render() {
        return (

            <MDBContainer fluid>
                <MDBRow>
                    <MDBCol md={2}>

                    </MDBCol>
                    <MDBCol md={8}>
                        <MDBRow>
                            <MDBCol md={10}>
                                <MDBInput label="Material input"/>
                            </MDBCol>
                            <MDBCol><MDBBtn floating size="lg" gradient="purple">
                                <MDBIcon icon="tools" size="2x"/>
                            </MDBBtn></MDBCol>
                        </MDBRow>
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
