import React, { useState, useEffect } from 'react';
import HomeTopMoviesComponent from './HomeTopMoviesComponent';


export default function HomeMoviesComponent(props) {

    const [homeMovies, setHomeMovies] = useState({})
    const [homeShows, setHomeShows] = useState([])
    let state = {
        isLoading: true
    }
    
    const getHomeMovies = async function () {
        const response = await fetch('http://127.0.0.1:5000/api/movify/v1/home');
        const responseJson = await response.json();
        const [movie_details, tv_shows] = Object.values(responseJson);
        setHomeMovies(movie_details);
        setHomeShows(tv_shows);
        state.isLoading = false;
      }
    
      useEffect(() => {
          getHomeMovies()
      }, [])

    console.log(props);

    if (!homeMovies.length) {
        return (
            <img className="spinner" src={props.Spinner} alt="spinner" />
          );
    }
    return (
        <HomeTopMoviesComponent Movies={homeMovies.top_movies} Spinner={props.Spinner}/>
    ); 
    

}