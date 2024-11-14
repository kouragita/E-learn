// src/components/Ratings.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Ratings({ learningPathId }) {
  const [rating, setRating] = useState(null);
  const [averageRating, setAverageRating] = useState(null);

  useEffect(() => {
    axios.get(`/api/ratings/${learningPathId}`)
      .then(response => setAverageRating(response.data.average))
      .catch(error => console.error("Error fetching average rating:", error));
  }, [learningPathId]);

  const handleRatingSubmit = (e) => {
    e.preventDefault();
    axios.post('/api/ratings', {
      learning_path_id: learningPathId,
      rating,
    })
      .then(response => {
        setAverageRating(response.data.new_average);
        setRating(null);
      })
      .catch(error => console.error("Error submitting rating:", error));
  };

  return (
    <div>
      <h3>Rate this Learning Path</h3>
      <p>Average Rating: {averageRating}</p>
      <form onSubmit={handleRatingSubmit}>
        <input
          type="number"
          min="1"
          max="5"
          value={rating || ""}
          onChange={(e) => setRating(Number(e.target.value))}
          placeholder="Rate (1-5)"
        />
        <button type="submit">Submit Rating</button>
      </form>
    </div>
  );
}

export default Ratings;
