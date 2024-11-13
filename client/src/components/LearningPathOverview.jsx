import React, { useEffect, useState } from 'react';
import PathCard from './PathCard';

function LearningPathOverview() {
  const [learningPaths, setLearningPaths] = useState([]);

  useEffect(() => {
    // Fetch learning paths from backend
    const fetchPaths = async () => {
      const response = await fetch('/api/learning_paths'); // adjust API endpoint as needed
      const data = await response.json();
      setLearningPaths(data);
    };
    fetchPaths();
  }, []);

  const handleFollow = async (pathId) => {
    try {
      await fetch(`/api/follow/${pathId}`, { method: 'POST' });
      console.log(`Followed path with id: ${pathId}`);
    } catch (error) {
      console.error("Error following path:", error);
    }
  };

  return (
    <div>
      <h2>Popular Learning Paths</h2>
      <div className="path-list">
        {learningPaths.map((path) => (
          <PathCard key={path.id} path={path} onFollow={handleFollow} />
        ))}
      </div>
    </div>
  );
}

export default LearningPathOverview;
