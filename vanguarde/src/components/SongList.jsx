import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {SongCard} from './SongCard.jsx';
import {MDBBtn, MDBCol, MDBContainer,
    MDBIcon, MDBInput, MDBRow} from 'mdbreact';

import {connect} from 'react-redux';
import {SearchOptions} from './SearchOptions';
import {toggleSearchBar} from '../reducers/searchReducer';
import {getSongList} from '../reducers/songReducer';
import {handleSearchChange} from '../reducers/searchReducer';

class SongList extends Component {
    static propTypes = {
        // methods
        getSongList: PropTypes.func.isRequired,
        toggleSearchBar: PropTypes.func.isRequired,
        handleSearchChange: PropTypes.func.isRequired,
        // fields
        searchBarIsVisible: PropTypes.bool.isRequired,
        songList: PropTypes.array,
    }

    componentDidMount() {
        console.log('componentDidMount');
        this.props.getSongList();
    }

    render() {
        return (
            <MDBContainer>
                <MDBRow className="d-flex flex-row">
                    <MDBCol md="10">
                        <MDBInput label="Search" onChange={this.props.handleSearchChange}/>
                    </MDBCol>
                    <MDBCol md="2">
                        <MDBBtn floating size="lg"
                            color="elegant"
                            onClick={this.props.toggleSearchBar}>
                            <MDBIcon icon="tools" size="2x"/>
                        </MDBBtn>
                    </MDBCol>
                </MDBRow>
                {this.props.searchBarIsVisible ?
                    <SearchOptions/> :
                    null}
                {this.props.songList.map((value, index) => {
                    const trackName = value.name;
                    return <SongCard key={index} artist="Someone cool" trackName={trackName}/>;
                })}
            </MDBContainer>
        );
    }
}

const mapStateToProps = (state) => ({
    songList: state.songReducer.songList,
    searchBarIsVisible: state.searchReducer.searchBarIsVisible,
});

export default connect(mapStateToProps,
    {getSongList, toggleSearchBar, handleSearchChange},
)(SongList);
