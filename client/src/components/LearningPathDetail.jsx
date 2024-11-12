import React, { useEffect, useState } from 'react';
import '../App.css';

const LearningPathDetail = ({ pathId, onBack }) => {
  const [pathDetails, setPathDetails] = useState(null);

  useEffect(() => {
    // Fetch the detailed information for the selected learning path
    fetch(`/api/learning-paths/${pathId}`)
      .then(response => response.json())
      .then(data => setPathDetails(data))
      .catch(error => console.error('Error fetching path details:', error));
  }, [pathId]);

  if (!pathDetails) return <p>Loading...</p>;

  return (
    <div className="learning-path-detail">
      <button onClick={onBack}>&larr; Back</button>
      <h2>{pathDetails.title}</h2>
      <p>{pathDetails.description}</p>
      
      <h3>Modules</h3>
      <ul className="modules-list">
        {pathDetails.modules.map(module => (
          <li key={module.id}>
            <h4>{module.title}</h4>
            <p>{module.description}</p>
            <ul>
              {module.resources.map(resource => (
                <li key={resource.id}>{resource.name} - {resource.type}</li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default LearningPathDetail;
