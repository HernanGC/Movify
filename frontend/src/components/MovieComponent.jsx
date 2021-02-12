import React, {useState, useEffect} from 'react';

export default function MovieComponent() {
    const [movies, setMovies] = useState({});

    const getMovies = async function () {
        let params = {
            movie: 'star wars'
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
        if (responseJson.Search) {
            setMovies(responseJson.Search)
            console.log(responseJson.Search);
        }
        return responseJson;
    }

    console.log(movies);

    useEffect(() => {
        getMovies();
    }, []);

    return (
        <>
         {Object.keys(movies).map(key =>
        <div className="col-2 movie-container">
            <p className="movie-title">{movies[key].Title}</p>
            <img src={movies[key].Poster} alt="" className="movie-img"/>
        </div> )}
        </>    
    );
}
