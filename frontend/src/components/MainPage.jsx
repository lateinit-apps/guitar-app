import React, { Component } from "react";
import {MDBBtn, MDBCard, MDBCardBody, MDBCol, MDBContainer, MDBIcon, MDBInput, MDBRow} from "mdbreact";
import placeholder from "../../public/150.png";


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
                        <MDBRow>
                            <MDBCol md={3}>
                                <img src={placeholder} alt="thumbnail"
                                     className="img-fluid img-thumbnail rounded float-right"
                                     style={{height: "150px"}}/>
                            </MDBCol>
                            <MDBCol md={8}>
                                <MDBCard className="align-middle" style={{height: "100px"}}>
                                    <MDBCardBody>
                                        sdfsf
                                    </MDBCardBody>
                                </MDBCard>
                            </MDBCol>
                            <MDBCol md={1}><MDBIcon className="float-left" icon="download" size="2x"/></MDBCol>
                        </MDBRow>
                    </MDBCol>
                    <MDBCol md={2}>
                    </MDBCol>
                </MDBRow>
            </MDBContainer>


        );

    }

}

export default MainPage;
