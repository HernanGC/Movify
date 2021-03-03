import React, { useEffect } from 'react';

export default function HomeTopMoviesComponent(props) {
    let movies = props.movies
    useEffect(() => {
        props.movies;
    }, movies = props.movies)
    console.log(props.movies);
    if (props.movies) {
        return (
            <>
           {Object.keys(props.movies).map(movie => {  
           <div>
               <h1>Top Movies</h1>
               <div className="col-xs-12 col-sm-6 col-md-4 col-lg-3 col-xl-2 movie-container">
               <p key={props.Title} className="movie-title hidden">{props.Title}</p>
               <img src={props.Poster} alt="" className="movie-img"/>
           </div>
           </div>
           })} 
           </>
   );
    } else {
        return (
            <img className="spinner" src={props.Spinner} alt="spinner" />
          );
    }
    
}