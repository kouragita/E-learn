import React, { useEffect, useState } from 'react';
import LearningPathDetail from './LearningPathDetail';

function LearningPathOverview() {
  const [learningPaths, setLearningPaths] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch learning paths from the backend
  useEffect(() => {
    const fetchLearningPaths = async () => {
      try {
        const response = await fetch('https://e-learn-ncux.onrender.com/api/learning_paths');
        if (!response.ok) {
          throw new Error(`Error: ${response.statusText}`);
        }
        const data = await response.json();
        setLearningPaths(data);  // Expecting a list of learning path objects
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchLearningPaths();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="learningpath">
      <h2>Welcome to Learning Paths</h2>
      {learningPaths.length > 0 ? (
        learningPaths.map((path) => (
          <LearningPathDetail key={path.id} path={path} />
        ))
      ) : (
        <div>No Learning Paths available.</div>
      )}
    </div>
  );
}

export default LearningPathOverview;
