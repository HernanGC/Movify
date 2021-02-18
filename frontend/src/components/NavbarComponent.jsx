import React from 'react';
import SearchComponent from './SearchComponent';


export default function NavbarComponent(props) {
    return (
        <>
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <div className="container-fluid">
                <a className="navbar-brand" href="#">Movify</a>
                <SearchComponent searchValue={props.searchValue} setSearchValue={props.setSearchValue}/>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="d-flex flex-row-reverse">
                    <div className="collapse navbar-collapse" id="navbarNavDropdown">
                        <ul className="navbar-nav">
                            <li className="nav-item">
                                <a className="nav-link active" aria-current="page" href="#">Home</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link" href="#">Tv Shows</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link" href="#">Movies</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </nav>
        </>
    );
}