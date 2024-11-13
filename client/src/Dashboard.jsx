// src/components/Dashboard.js
import React from 'react';
import { getCurrentUser, logout } from './authService';
import { useNavigate } from 'react-router-dom';

function Dashboard() {
  const user = getCurrentUser();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div>
      <h2>Welcome, {user?.username}</h2>
      <p>Role: {user?.role}</p>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
}

export default Dashboard;
