import React from 'react';

export default function SeachComponent(props) {

    const handleSubmit = function (e) {
        e.preventDefault();
        props.setSearchValue(e.target.childNodes[0].value)
    }

    return (
        <>
        <form
        className="movie-search-form"  
        onSubmit={(e) => handleSubmit(e)}>
            <input 
            className="form-control" 
            type="search" 
            placeholder="Search" 
            aria-label="Search"/>
        </form>
        </>
    )
}