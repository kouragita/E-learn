import React from 'react';

function ResourceList({ resources }) {
  return (
    <div className="resources">
      <h5>Resources</h5>
      {resources.map((resource) => (
        <div key={resource.id} className="resource">
          <p>{resource.type}: {resource.title}</p>
          <p>{resource.description}</p>
          <a href={resource.url} target="_blank" rel="noopener noreferrer">View Resource</a>
        </div>
      ))}
    </div>
  );
}

export default ResourceList;
