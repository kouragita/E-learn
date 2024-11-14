import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LearningPathOverview from './components/LearningPathOverview';
import LearningPathDetail from './components/LearningPathDetail';
import CreateLearningPathForm from './components/CreateLearningPathForm';
import Challenges from './components/Challenges';
import Rewards from './components/Rewards';
import EventHighlights from './components/EventHighlights';
import ModuleDetail from './components/ModuleDetail';
import ResourceDetail from './components/ResourceDetail';
import QuizDetail from './components/QuizDetail';

function App() {
  return (
    <Router>
      <Routes>
        {/* Route for the Learning Path Overview */}
        <Route path="/" element={<LearningPathOverview />} />

        {/* Route for the Learning Path Detail */}
        <Route path="/learning-path/:pathId" element={<LearningPathDetail />} />

        {/* Route for a specific Module within a Learning Path */}
        <Route path="/learning-path/:pathId/module/:moduleId" element={<ModuleDetail />} />

        {/* Route for a specific Resource within a Module */}
        <Route path="/learning-path/:pathId/module/:moduleId/resource/:resourceId" element={<ResourceDetail />} />

        {/* Route for a specific Quiz within a Learning Path */}
        <Route path="/learning-path/:pathId/quiz/:quizId" element={<QuizDetail />} />

        {/* Route for Create Learning Path Form */}
        <Route path="/create-learning-path" element={<CreateLearningPathForm />} />

        {/* Route for Challenges */}
        <Route path="/challenges" element={<Challenges />} />

        {/* Route for Rewards */}
        <Route path="/rewards" element={<Rewards />} />

        {/* Route for Event Highlights */}
        <Route path="/events" element={<EventHighlights />} />
      </Routes>
    </Router>
  );
}

export default App;
