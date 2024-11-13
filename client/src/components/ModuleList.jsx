import React from 'react';
import ResourceList from './ResourceList';
import QuizList from './QuizList';

function ModuleList({ modules }) {
  return (
    <div>
      <h3>Modules</h3>
      {modules.map((module) => (
        <div key={module.id} className="module">
          <h4>{module.title}</h4>
          <p>{module.description}</p>
          <ResourceList resources={module.resources} />
          <QuizList quizzes={module.quizzes} />
        </div>
      ))}
    </div>
  );
}

export default ModuleList;
