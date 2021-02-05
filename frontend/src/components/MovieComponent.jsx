import React from 'react';

class MovieComponent extends React.Component {
    render() {
        return <div>
                    <h1>{this.props.title}</h1>
                    <img src={this.props.poster}/>    
                </div>
        
    }
}

export default MovieComponent;