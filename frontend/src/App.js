import logo from './logo.svg';
import './App.css';
import IndexComponent from './components/IndexComponent';
import NavbarComponent from './components/NavbarComponent';
import MovieComponent from './components/MovieComponent';
import 'bootswatch/dist/lux/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import {
   BrowserRouter as Router,
   Switch,
   Route,
   Link
  } from 'react-router-dom';


function App() {
  return (
    <div className="App">
      <NavbarComponent />
      <IndexComponent name='Movify' />
      <div className='container-fluid'>
        <div className="row justify-content-md-center">
          <MovieComponent />
        </div>
      </div>
    </div>
  );
}

export default App;
