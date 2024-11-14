// src/components/Comments.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Comments({ learningPathId }) {
  const [comments, setComments] = useState([]);
  const [newComment, setNewComment] = useState('');

  useEffect(() => {
    axios.get(`/api/comments/${learningPathId}`)
      .then(response => setComments(response.data))
      .catch(error => console.error("Error fetching comments:", error));
  }, [learningPathId]);

  const handleAddComment = () => {
    axios.post('/api/comments', {
      learning_path_id: learningPathId,
      content: newComment,
    })
      .then(response => {
        setComments([...comments, response.data]);  // add new comment to list
        setNewComment('');  // clear the input
      })
      .catch(error => console.error("Error adding comment:", error));
  };

  return (
    <div>
      <h3>Comments</h3>
      {comments.map((comment, index) => (
        <p key={index}>{comment.content}</p>
      ))}
      <textarea
        value={newComment}
        onChange={(e) => setNewComment(e.target.value)}
        placeholder="Add a comment"
      />
      <button onClick={handleAddComment}>Post Comment</button>
    </div>
  );
}

export default Comments;
