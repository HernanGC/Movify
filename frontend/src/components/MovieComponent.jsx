import React, {useState, useEffect} from 'react';

export default function MovieComponent(props) {


    return (
        <>
         {Object.keys(props.movies).map(key =>
        <div className="col-xs-12 col-sm-6 col-md-4 col-lg-3 col-xl-2 movie-container" >
            <p className="movie-title hidden">{props.movies[key].Title}</p>
            <img src={props.movies[key].Poster} alt="" className="movie-img"/>
        </div> )}
        </>    
    );
}
