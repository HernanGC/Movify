import React, { useEffect } from 'react';

export default function HomeTopMoviesComponent(props) {
    // console.log(props);
    const moviesList = props.Movies.map((movie) => 
        <div key={props.Movies.indexOf(movie)} className="col-xs-12 col-sm-6 col-md-4 col-lg-3 col-xl-2 movie-container">
            <p key={movie.Title} className="movie-title hidden">{movie.Title}</p>
            <img src={movie.Poster} alt="" className="movie-img"/>
        </div>
        );

        console.log('coso');

    if (props.Movies) {
        return (
            <>
           <div>
               <h1>Top Movies</h1>
               {moviesList}
           </div> 
           </>
   );
    } else {
        return (
            <img className="spinner" src={props.Spinner} alt="spinner" />
          );
    }
    
}