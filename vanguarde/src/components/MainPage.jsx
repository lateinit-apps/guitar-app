import React, { Component } from "react";
import {MDBCol, MDBContainer, MDBRow} from "mdbreact";

class MainPage extends Component {

    render() {
        return (

            <MDBContainer fluid>
                <MDBRow>
                    <MDBCol md="2">

                    </MDBCol>
                    <MDBCol md="8">
                        <SongList/>
                    </MDBCol>
                    <MDBCol md="2">
                    </MDBCol>
                </MDBRow>
            </MDBContainer>

        );

    }

}

export default MainPage;
