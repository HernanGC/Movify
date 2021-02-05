import logo from './logo.svg';
import './App.css';
import IndexComponent from './components/IndexComponent';
import NavbarComponent from './components/NavbarComponent';
import MovieComponent from './components/MovieComponent';
import 'bootswatch/dist/lux/bootstrap.min.css';
import {
   BrowserRouter as Router,
   Switch,
   Route,
   Link
  } from 'react-router-dom';

const state = {
  title: 'Star Wars: Episode IV - A New Hope',
  poster: 'https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg'
};

const getMovie = async () => {
  const url = 'http://www.omdbapi.com/?s=star%20wars&apikey=dffc746e';
  const response = await fetch(url);
  const responseJson = await response.json();
  if (responseJson.Search) {
    const firstObject = Object.values(responseJson.Search)[0];
    state.title = firstObject.Title;
    state.poster = firstObject.Poster;
    console.log(state.poster);
  }
}


getMovie();



function App() {
  return (
    <div className="App">
      <NavbarComponent />
      <IndexComponent name='Netflix' />
      <MovieComponent title={state.title} poster={state.poster} />
    </div>
  );
}

export default App;
