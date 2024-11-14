// src/components/DiscussionThread.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function DiscussionThread({ learningPathId }) {
  const [threads, setThreads] = useState([]);
  const [newThreadTitle, setNewThreadTitle] = useState('');
  const [newThreadContent, setNewThreadContent] = useState('');

  useEffect(() => {
    axios.get(`/api/discussions/${learningPathId}`)
      .then(response => setThreads(response.data))
      .catch(error => console.error("Error fetching discussions:", error));
  }, [learningPathId]);

  const handleAddThread = () => {
    axios.post('/api/discussions', {
      learning_path_id: learningPathId,
      title: newThreadTitle,
      content: newThreadContent
    })
      .then(response => {
        setThreads([...threads, response.data]);
        setNewThreadTitle('');
        setNewThreadContent('');
      })
      .catch(error => console.error("Error adding discussion:", error));
  };

  return (
    <div>
      <h3>Discussions</h3>
      {threads.map((thread) => (
        <div key={thread.id}>
          <h4>{thread.title}</h4>
          <p>{thread.content}</p>
          {/* Additional component for replies can be nested here */}
        </div>
      ))}
      <input
        type="text"
        value={newThreadTitle}
        onChange={(e) => setNewThreadTitle(e.target.value)}
        placeholder="Thread Title"
      />
      <textarea
        value={newThreadContent}
        onChange={(e) => setNewThreadContent(e.target.value)}
        placeholder="Start a new discussion"
      />
      <button onClick={handleAddThread}>Post Thread</button>
    </div>
  );
}

export default DiscussionThread;
