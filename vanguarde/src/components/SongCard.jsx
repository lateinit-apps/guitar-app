import {
    MDBCard,
    MDBCardBody,
    MDBContainer, MDBRow, MDBIcon, MDBBtn, MDBCol
} from "mdbreact";
import React, {Component} from "react";
import placeholder from "../assets/150.png";

export class SongCard extends Component {

    render() {
        return (

            <MDBRow className="pl-0">
                    <MDBCol md="10">
                        <MDBCard className="align-middle mb-3 text-left">
                            <div  className="row no-gutters">
                                <div className="col-md-1" style={{minWidth: "150px"}}>
                                    <img src={placeholder} alt="thumbnail"
                                    />
                                </div>
                                <div className="col-md-6">
                                    <div className="card-body">
                                        <h4 className="card-title">{this.props.artist} -  {this.props.trackName} </h4>
                                    </div>
                                </div>
                            </div>
                        </MDBCard>
                    </MDBCol>
                    <MDBCol md="2">
                        <MDBBtn className="alignRight" color="elegant">
                            <MDBIcon className="float-left" icon="download" size="2x"/>
                        </MDBBtn>
                    </MDBCol>

            </MDBRow>

        );
    }
}