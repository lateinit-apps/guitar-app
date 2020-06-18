import React, { Component } from "react";
import {SongCard} from "./SongCard.jsx";
import {MDBBtn, MDBCol, MDBContainer, MDBIcon, MDBInput, MDBRow} from "mdbreact";
import {SearchOptions} from "./SearchOptions";
import {getSongList} from "../actions/songList";

import { connect } from 'react-redux';

// import axios from "axios";
// import { FETCH_SONG_LIST_SUCCESS } from "../constants/action-types";
// import { fetchBegin, fetchError, handleError } from "./actions/index";


class MainPage extends Component {

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
        return (

            <MDBContainer fluid>
                <MDBRow>
                    <MDBCol md="2">

                    </MDBCol>
                    <MDBCol md="8">
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
                        {/* <SongCard artist="Some cool dude" trackName="Some cool track"/> */}
                        {/* <SongCard artist="Взрвыв кабачка в коляске с поносом" trackName="Мрачный аборт в сарае"/> */}
                    </MDBCol>
                    <MDBCol md="2">
                    </MDBCol>
                </MDBRow>
            </MDBContainer>


        );

    }

}

const mapStateToProps = (state) => ({
    songList: state.songReducer.songList
});

export default connect(mapStateToProps, {getSongList})(MainPage);
