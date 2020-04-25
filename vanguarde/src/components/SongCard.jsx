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
            // <div className="card mb-3" style="max-width: 540px;">
            //     <div className="row no-gutters">
            //         <div className="col-md-4">
            //             <img src={placeholder} alt="thumbnail"
            //             />
            //         </div>
            //         <div className="col-md-8">
            //             <div className="card-body">
            //                 <h5 className="card-title">Card title</h5>
            //                 <p className="card-text">This is a wider card with supporting text below as a natural
            //                     lead-in to additional content. This content is a little bit longer.</p>
            //                 <p className="card-text"><small className="text-muted">Last updated 3 mins ago</small></p>
            //             </div>
            //         </div>
            //     </div>
            // </div>

            <MDBContainer>
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