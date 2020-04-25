import {
    MDBCard,
    MDBCardBody,
    MDBContainer, MDBRow, MDBIcon, MDBBtn
} from "mdbreact";
import React, {Component} from "react";
import placeholder from "../assets/150.png";

export class SongCard extends Component {

    render() {
        return (

            <MDBContainer fluid className={'pl-0'}>
                <MDBCard className="align-middle mb-3 text-left" style={{maxWidth: "700px"}}>
                    <div className="row no-gutters">
                        <div className="col-md-3">
                            <img src={placeholder} alt="thumbnail"
                            />
                        </div>
                        <div className="col-md-9">
                            <div className="card-body">
                                <h5 className="card-title">{this.props.artist} -  {this.props.trackName} </h5>
                            </div>
                        </div>
                    </div>
                </MDBCard>
                <MDBBtn className={"alignRight"} color="elegant">
                    <MDBIcon className="float-left" icon="download" size="2x"/>
                </MDBBtn>

            </MDBContainer>

        );
    }
}