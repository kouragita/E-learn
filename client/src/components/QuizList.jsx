import React from 'react';

function QuizList({ quizzes }) {
  return (
    <div className="quizzes">
      <h5>Quizzes</h5>
      {quizzes.map((quiz) => (
        <div key={quiz.id} className="quiz">
          <p>{quiz.question}</p>
          {quiz.options && quiz.options.map((option, index) => (
            <div key={index}>
              <input type="radio" name={`quiz-${quiz.id}`} value={option} />
              <label>{option}</label>
            </div>
          ))}
        </div>
      ))}
    </div>
  );
}

export default QuizList;
