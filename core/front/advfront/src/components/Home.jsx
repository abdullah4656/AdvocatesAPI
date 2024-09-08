import { Link } from 'react-router-dom';
import axios from 'axios';
import React, { useState, useEffect } from 'react';

const Home = () => {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);
  const [query, setQuery] = useState('');

  const getData = async (query = '') => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/list/?query=${query}`);
      console.log(response.data); // Log the response data here
      setData(response.data);
    } catch (error) {
      setError(error);
    }
  };

  const searchData = (e) => {
    e.preventDefault();
    let query=e.target.query.value
    getData(query);
  };

  const handleQueryChange = (e) => {
    setQuery(e.target.value);
  };

  useEffect(() => {
    getData();
  }, []);

  return (
    <div className='wrapper'>
      <h1>Search Developers According to Your needs</h1>
      <form id="search-form" onSubmit={searchData}>
        <input className="enter" type="text" name="query" value={query} onChange={handleQueryChange} placeholder='Search Advocates' />
        <input type="submit" className='sub' value="Search" />
      </form>
      {error ? (
        <div>Error: {error.message}</div>
      ) : (
        <div className='Advocate_list'>
          {data.map(item => (
            <div className='container' key={item.id}>
              <Link to={`/adv/${item.username}`}> <img className='profile' src={`http://127.0.0.1:8000${item.img}`} alt="adv image" />
              </Link>
              <h2> <strong>{item.username}</strong></h2>
              <p>{item.bio}</p>
              <p>{item.followers}</p>
              <a href={item.twitterlink}>@{item.username}</a>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Home;