
import { useState } from 'react';
import Footer from './components/Footer';
import Leaderboard from './components/Leaderboard';
import UserProfile from './components/UserProfile';

import './App.css';

function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      <main className="flex-grow container mx-auto px-4 py-8">
        <div className="space-y-8">
          <UserProfile />
          <Leaderboard />
        </div>
      </main>
      <Footer />
    </div>
  );
}

export default App;

