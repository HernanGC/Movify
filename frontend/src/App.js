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

let obj = {};

const state = {
  title: 'Star Wars: Episode IV - A New Hope',
  poster: 'https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg'
};

const getMovie = async () => {
  let params = {
    movie: 'star wars'
  }
  console.log(JSON.stringify(params));
  const url = 'http://127.0.0.1:5000/api/movify/v1/search';
  /** The API receives a JSON object, so headers must contain content-type: application/json */
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(params)
  });
  const responseJson = await response.json();
  if (responseJson.Response == 'True') {
    obj = responseJson.Search;
  }
  console.log(obj);
  return await handleData(responseJson);
  console.log(responseJson);
  // if (responseJson.Search) {
    // const firstObject = Object.values(responseJson.Search)[0];
    // state.title = firstObject.Title;
    // state.poster = firstObject.Poster;
    // console.log(state);
  // }
}

const handleData = async function(temp1) {
  let arr = [];
  Object.keys(temp1).forEach(key => {
    arr += temp1[key]['Title'];
  });
  return arr;
}


console.log(getMovie());



function App() {
  return (
    <div className="App">
      <NavbarComponent />
      <IndexComponent name='Movify' />
      <MovieComponent movies={getMovie()} />
    </div>
  );
}

export default App;
