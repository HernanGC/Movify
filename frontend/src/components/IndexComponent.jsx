import React from 'react';

class IndexComponent extends React.Component {
    render() {
        return <h1 className="hello">{this.props.name}</h1>
    }
}

export default IndexComponent;