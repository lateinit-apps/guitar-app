import React, {Component} from 'react';
import {MDBCol, MDBContainer, MDBInput,
    MDBRow, MDBCard, MDBAnimation} from 'mdbreact';
import PropTypes from 'prop-types';
import {connect} from 'react-redux';
import {changeSearchQuery} from '../redux/search';
import {ARTIST_QUERY, RELEASE_QUERY, SONG_QUERY, GENRE_QUERY} from '../redux/search';
import Select from 'react-select';


const genreOptions = [
    {value: 'rock', label: 'Rock'},
    {value: 'notrock', label: 'Not Rock'},
];

class SearchOptions extends Component {
    static propTypes = {
        // methods
        changeSearchQuery: PropTypes.func.isRequired,
    }

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
                                            <MDBInput label="Artist name"
                                                onChange={
                                                    (event) => {
                                                        this.props.changeSearchQuery(ARTIST_QUERY, event.target.value);
                                                    }
                                                } group/>
                                            <MDBInput label="Song name"
                                                onChange={
                                                    (event) => {
                                                        this.props.changeSearchQuery(SONG_QUERY, event.target.value);
                                                    }
                                                }
                                                group />
                                        </div>
                                    </form>
                                </MDBCol>
                                <MDBCol md="6">
                                    <div className="grey-text">
                                        <MDBInput label="Album"
                                            onChange={
                                                (event) => {
                                                    this.props.changeSearchQuery(RELEASE_QUERY, event.target.value);
                                                }
                                            }
                                            group/>
                                        <Select onChange={
                                            (option) => {
                                                this.props.changeSearchQuery(GENRE_QUERY, option.value);
                                            }
                                        }
                                        options={genreOptions} />
                                    </div>
                                </MDBCol>
                            </MDBRow>
                        </MDBCard>
                    </MDBCol>
                </MDBContainer>

            </MDBAnimation>
        );
    }
}

const mapStateToProps = (state) => ({});

export default connect(mapStateToProps,
    {changeSearchQuery},
)(SearchOptions);

