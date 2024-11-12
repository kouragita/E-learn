 // src/components/LearningPaths.js
import React, { useEffect, useState } from 'react';
import CreatePathForm from './CreatePathForm';
import EnrollPathForm from './EnrollPathForm';
import LearningPathDetail from './LearningPathDetail';
import '../App.css';

const LearningPaths = () => {
  const [learningPaths, setLearningPaths] = useState([]);
  const [selectedPath, setSelectedPath] = useState(null);

  useEffect(() => {
    // Fetch all learning paths from the backend
    fetch('/api/learning-paths')
      .then(response => response.json())
      .then(data => setLearningPaths(data))
      .catch(error => console.error('Error fetching learning paths:', error));
  }, []);

  const handleAddPath = (newPath) => {
    setLearningPaths([...learningPaths, newPath]);
  };

  const viewPathDetail = (pathId) => {
    setSelectedPath(pathId);
  };

  return (
    <div className="container">
      <h1 className="title">Learning Paths</h1>

      {selectedPath ? (
        <LearningPathDetail pathId={selectedPath} onBack={() => setSelectedPath(null)} />
      ) : (
        <>
          <ul className="learning-paths-list">
            {learningPaths.map(path => (
              <li key={path.id} className="learning-path-item">
                <h3>{path.title}</h3>
                <p>{path.description}</p>
                <button onClick={() => viewPathDetail(path.id)}>View Details</button>
              </li>
            ))}
          </ul>

          <h2 className="section-title">Create a New Path</h2>
          <CreatePathForm onAddPath={handleAddPath} />

          <h2 className="section-title">Enroll in a Path</h2>
          <EnrollPathForm paths={learningPaths} />
        </>
      )}
    </div>
  );
};

export default LearningPaths;
