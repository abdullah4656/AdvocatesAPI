import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { Link } from 'react-router-dom';
import './adv.css';
const Advocatepage = () => {
  const params = useParams();
  const username = params.username;
  const [advocate, setAdvocate] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/list/${username}`);
        console.log(response.data); // Log the response data here
        setAdvocate(response.data);
      } catch (error) {
        setError(error);
      }
    }
    fetchData();
  }, [username]);

  return (
    <>
    <div>
 {advocate&&(
  <div className='container-adv' key={advocate.id}>
  <Link to={`/adv/${advocate.username}`}> <img className='profile-adv' src={`http://127.0.0.1:8000${advocate.img}`} alt="adv image" />      
  </Link>
<h2>     <strong>{advocate.username}</strong></h2>
  
  <p>{advocate.bio}</p>
  <p>{advocate.followers}</p>

</div>
 )}
 </div>
    </>
  );
};

export default Advocatepage;