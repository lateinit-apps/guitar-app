import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {SongCard} from './SongCard.jsx';
import {MDBBtn, MDBCol, MDBContainer,
    MDBIcon, MDBInput, MDBRow} from 'mdbreact';

import {connect} from 'react-redux';
import {SearchOptions} from './SearchOptions';
import {toggleSearchBar, handleSearchChange, handleSortToggle} from '../redux/search';
import {getSongList} from '../redux/songs';

class SongList extends Component {
    static propTypes = {
        // methods
        getSongList: PropTypes.func.isRequired,
        toggleSearchBar: PropTypes.func.isRequired,
        handleSearchChange: PropTypes.func.isRequired,
        handleSortToggle: PropTypes.func.isRequired,
        // fields
        searchBarIsVisible: PropTypes.bool.isRequired,
        songList: PropTypes.array,
        sorting: PropTypes.string,
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
                        <MDBBtn size="lg"
                            color="elegant"
                            onClick={this.props.toggleSearchBar}>
                            <MDBIcon icon="tools" size="2x"/>
                        </MDBBtn>
                    </MDBCol>
                </MDBRow>
                <MDBRow>
                    <MDBBtn
                        color="elegant"
                        onClick={this.props.handleSortToggle}
                    >
                        <MDBIcon
                            icon={
                                this.props.sorting === 'asc' ? 'sort-amount-down' : 'sort-amount-up'
                            }
                            size="2x"/>
                    </MDBBtn>
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
    sorting: state.searchReducer.sorting,
});

export default connect(mapStateToProps,
    {getSongList, toggleSearchBar, handleSearchChange, handleSortToggle},
)(SongList);
