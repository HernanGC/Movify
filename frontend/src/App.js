import React, {useState, useEffect} from 'react';
import Spinner from './Spinner.svg';
import './App.css';
import IndexComponent from './components/IndexComponent';
import NavbarComponent from './components/NavbarComponent';
import MovieComponent from './components/MovieComponent';
import 'bootstrap/dist/js/bootstrap.js';
import 'bootswatch/dist/lux/bootstrap.min.css';
import 'popper.js';
import 'jquery';


import {
   BrowserRouter as Router,
   Switch,
   Route,
   Link
  } from 'react-router-dom';


function App() {
  const [movies, setMovies] = useState({});
  const [searchValue, setSearchValue] = useState('');

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
        // console.log(responseJson)
        if (responseJson) {
            setMovies(responseJson)
        }

        return responseJson;
    }

    useEffect(() => {
        getMovies();
    }, [searchValue]);

  console.log(movies);

  return (
    <div className="App">
      <NavbarComponent searchValue={searchValue} setSearchValue={setSearchValue}/>
      {/* <IndexComponent name='Movify' /> */}
      <div className='container-fluid'>
        <div className="row justify-content-md-center">
          <MovieComponent movies={movies} Spinner={Spinner}/>
        </div>
      </div>
    </div>
  );
}

export default App;
