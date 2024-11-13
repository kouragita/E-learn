// src/services/authService.js
import axios from 'axios';

const API_URL = 'http://localhost:5000/api'; // Replace with your backend URL

// Register a new user
export const register = async (userData) => {
  return axios.post(`${API_URL}/auth/register`, userData);
};

// Login a user
export const login = async (userData) => {
  return axios.post(`${API_URL}/auth/login`, userData);
};

// Fetch current user
export const getCurrentUser = () => {
  return JSON.parse(localStorage.getItem('user'));
};

// Logout user
export const logout = () => {
  localStorage.removeItem('user');
};
