import React from 'react';

function PathCard({ path, onFollow }) {
  return (
    <div className="path-card">
      <h3>{path.title}</h3>
      <p>{path.description}</p>
      <p>Contributor: {path.contributor_id}</p>
      <button onClick={() => onFollow(path.id)}>Follow</button>
    </div>
  );
}

export default PathCard;
