import React, { Component } from "react";
import {MDBCol, MDBContainer, MDBInput, MDBRow, MDBCard, MDBAnimation} from "mdbreact";


export class SearchOptions extends Component {

    render() {
        return (
            <MDBAnimation type="fadeInUp">

                <MDBContainer className="mb-2 pl-0 ml-0">
                    <MDBCol md="9" className="pl-0">
                        <MDBCard>
                            <p className="h4 text-center py-4">Search filters</p>
                            <MDBRow className="ml-2 mr-2">
                                <MDBCol md="6">
                                    <form>
                                        <div className="grey-text">
                                            <MDBInput label="Artist name" group/>
                                            <MDBInput label="Song name" group />
                                        </div>
                                    </form>
                                </MDBCol>
                                <MDBCol md="6">
                                    <div className="grey-text">
                                        <MDBInput label="Something else" group/>
                                        <select className="browser-default custom-select">
                                            <option value="1">Rock</option>
                                            <option value="2">Not Rock</option>=
                                        </select>
                                    </div>
                                </MDBCol>
                            </MDBRow>
                        </MDBCard>
                    </MDBCol>
                </MDBContainer>

            </MDBAnimation>
        )
    }

}