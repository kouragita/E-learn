import { useState } from 'react'
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import NavBar from "./components/NavBar";
import Signup from './components/Auth/Signup';
import Login from './components/Auth/Login';
import Dashboard from './components/Dashboard';
import './App.css'
import LearningPathCard from './components/LearningPaths'
import LearningPaths from './components/LearningPaths'

function App() {

  return (
    <>
     <Router>
      <div>
        <NavBar/>
        <Routes>
          <Route path="/signup" element={<Signup />} />
          <Route path="/login" element={<Login />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </div>
    </Router>
      <div>
        <LearningPaths/>
      </div>
     
    </>
  )
}

export default App;
