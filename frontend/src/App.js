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


function App() {
  return (
    <div className="App">
      <NavbarComponent />
      <IndexComponent name='Movify' />
      <div className="row">
        <MovieComponent />
      </div>
    </div>
  );
}

export default App;
