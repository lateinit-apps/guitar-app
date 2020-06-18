import React, {Component} from "react";
import {MDBContainer, MDBFooter} from "mdbreact";

export class Footer extends Component {

    constructor(props){
        super(props);


        this.footerClicks = 0;
        this.footerArray = [
            '© ' + new Date().getFullYear() + ' Copyright Lateinit Apps',
            'Шёл медведь по лесу, видит - машина горит. Сел в неё и сгорел',
            'Copyright © 2007. All bears reserved.',
            'Надел мужик шляпу.',
            'А она ему как раз.',
            'It\'s a bird... It\'s a plane... No, it is a Songsterr clone!'
        ];

        this.state = {
            footerText: this.footerArray[0]
        };

        this.handleFooterClick = this.handleFooterClick.bind(this);

    }

    handleFooterClick(e){
        this.footerClicks += 1;
        if (this.footerClicks > 5){
            let newFooterText = this.footerArray[(this.footerClicks - 5) % this.footerArray.length];
            this.setState({footerText: newFooterText});
        }
    }

    render() {
        return (
            <MDBFooter color="elegant-color" className="font-small pt-4 mt-4 fixed-bottom" onClick={this.handleFooterClick}
                       style={{
                           WebkitTouchCallout: 'none',
                           WebkitUserSelect: 'none',
                           KhtmlUserSelect: 'none',
                           MozUserSelect: 'none',
                           MsUserSelect: 'none',
                           userSelect: 'none',
                       }}>
                <div className="footer-copyright text-center py-3">
                    <MDBContainer fluid >
                        {this.state.footerText}
                    </MDBContainer>
                </div>
            </MDBFooter>
        )
    }
}
