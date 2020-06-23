import React, { Component } from "react";
import {SongCard} from "./SongCard.jsx";
import {MDBBtn, MDBCol, MDBContainer, MDBIcon, MDBInput, MDBRow} from "mdbreact";

import { connect } from 'react-redux';
import {SearchOptions} from "./SearchOptions";
import {getSongList} from "../actions/songList";


class SongList extends Component {

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

    componentDidMount() {
        console.log("componentDidMount");
        this.props.getSongList();
    }

    render() {
        <MDBContainer>
            <MDBRow className="d-flex flex-row">
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
            {this.props.songList.map((value, index) => {
                let trackName = value.name
                return <SongCard artist="Someone cool" trackName={trackName}/>
            })}
        </MDBContainer>
    }

}

const mapStateToProps = (state) => ({
    songList: state.songReducer.songList
});

export default connect(mapStateToProps, {getSongList})(SongList);