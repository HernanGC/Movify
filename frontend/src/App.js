import React, {useState, useEffect} from 'react';
import Spinner from './Spinner.svg';
import './App.css';
import IndexComponent from './components/IndexComponent';
import NavbarComponent from './components/NavbarComponent';
import MovieComponent from './components/MovieComponent';
import HomeMoviesComponent from './components/HomeMoviesComponent';
import 'bootswatch/dist/lux/bootstrap.min.css';

import {
   BrowserRouter as Router,
   Switch,
   Route,
   Link
  } from 'react-router-dom';


function App() {

  const [homeMovies, setHomeMovies] = useState({})
  const [homeShows, setHomeShows] = useState([])
  const [movies, setMovies] = useState({});
  const [searchValue, setSearchValue] = useState('');


    const getHomeMovies = async function () {
      const response = await fetch('http://127.0.0.1:5000/api/movify/v1/home');
      const responseJson = await response.json();
      const [movie_details, tv_shows] = Object.values(responseJson);
      setHomeMovies(movie_details);
      setHomeShows(tv_shows);
      console.log(responseJson);
      console.log(movie_details);
      console.log(tv_shows);
    }

    const getMovies = async function () {
         let params = {
            movie: searchValue
        };
        const url = 'http://127.0.0.1:5000/api/movify/v1/search';

        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(params)
        });

        const responseJson = await response.json();
        if (responseJson) {
            setMovies(responseJson)
        }
        return responseJson;
    }

    useEffect(() => {
      getHomeMovies();
    }, []);


  return (
    <div className="App">
      <NavbarComponent searchValue={searchValue} setSearchValue={setSearchValue}/>
      {/* <IndexComponent name='Movify' /> */}
      <div className='container-fluid'>
        <div className="row justify-content-md-center">
          <HomeMoviesComponent movies={homeMovies} Spinner={Spinner}/>
          <MovieComponent movies={movies} Spinner={Spinner}/>
        </div>
      </div>
    </div>
  );
}

export default App;
