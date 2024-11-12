import React, { useState } from 'react';

const EnrollPathForm = ({ paths }) => {
  const [selectedPath, setSelectedPath] = useState('');
  const [enrollMessage, setEnrollMessage] = useState('');

  const handleEnroll = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(`/api/learning-paths/${selectedPath}/enroll`, {
        method: 'POST'
      });
      const data = await response.json();
      setEnrollMessage(`Successfully enrolled in ${data.title}!`);
    } catch (error) {
      console.error('Error enrolling in learning path:', error);
      setEnrollMessage('Failed to enroll. Please try again.');
    }
  };

  return (
    <form onSubmit={handleEnroll}>
      <select
        value={selectedPath}
        onChange={(e) => setSelectedPath(e.target.value)}
        required
      >
        <option value="">Select a Path</option>
        {paths.map(path => (
          <option key={path.id} value={path.id}>
            {path.title}
          </option>
        ))}
      </select>
      <button type="submit">Enroll</button>
      {enrollMessage && <p>{enrollMessage}</p>}
    </form>
  );
};

export default EnrollPathForm;
