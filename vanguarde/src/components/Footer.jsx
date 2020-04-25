import React, {Component} from "react";
import {MDBContainer, MDBFooter} from "mdbreact";

export class Footer extends Component {

    render() {
        return (
            <MDBFooter color="elegant-color" className="font-small pt-4 mt-4 fixed-bottom">
                <div className="footer-copyright text-center py-3">
                    <MDBContainer fluid>
                        &copy; {new Date().getFullYear()} Copyright LateInit Apps
                    </MDBContainer>
                </div>
            </MDBFooter>
        )
    }
}