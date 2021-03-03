import React from 'react';
import HomeTopMoviesComponent from './HomeTopMoviesComponent';

export default function HomeMoviesComponent(props) {
    const popularMovies = props.movies.popular_movies;
    const topMovies = props.movies.top_movies;
    console.log(props);
    return (
        <HomeTopMoviesComponent movies={topMovies}/>
    )
    

}