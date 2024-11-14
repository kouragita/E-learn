import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import ModuleDetail from './ModuleDetail';

function LearningPathDetail() {
  const [learningPath, setLearningPath] = useState(null);
  const [progress, setProgress] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const { pathId } = useParams();

  useEffect(() => {
    const fetchLearningPathDetails = async () => {
      try {
        const response = await fetch('https://e-learn-ncux.onrender.com/learning_paths/<int:id>');
        if (!response.ok) {
          throw new Error(`Error: ${response.statusText}`);
        }
        const data = await response.json();
        
        // Assuming the API returns both the learning path and progress information
        setLearningPath(data.learning_path);
        setProgress(data.progress);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchLearningPathDetails();
  }, [pathId]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h2>Details of Learning Path ID: {pathId}</h2>
      {learningPath ? (
        <div>
          <h3>{learningPath.title}</h3>
          <p>{learningPath.description}</p>
          <p>Contributor ID: {learningPath.contributor_id}</p>
          
          {/* Display User Progress */}
          {progress && (
            <div>
              <h4>Your Progress: {progress}%</h4>
              <p>Date Enrolled: {progress.date_enrolled}</p>
            </div>
          )}

          {/* Display Modules */}
          {learningPath.modules && learningPath.modules.length > 0 ? (
            learningPath.modules.map((module) => (
              <ModuleDetail key={module.id} module={module} />
            ))
          ) : (
            <p>No modules available for this learning path.</p>
          )}
        </div>
      ) : (
        <div>No details available for this learning path.</div>
      )}
    </div>
  );
}

export default LearningPathDetail;

