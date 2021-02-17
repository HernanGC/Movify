import React from 'react';

export default function SeachComponent(props) {

    const handleSubmit = function (e) {
        e.preventDefault();
        props.setSearchValue(e.target.value)
    }

    return (
        <>
        <input 
        className="form-control movie-search-input" 
        type="search" 
        placeholder="Search" 
        aria-label="Search"
        onChange= {(e) => handleSubmit(e)}/>
        </>
    )
}