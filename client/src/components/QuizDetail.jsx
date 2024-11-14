import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const QuizDetail = () => {
    const { pathId, quizId } = useParams();
    const [quiz, setQuiz] = useState(null);
    const [answers, setAnswers] = useState({});
    const [score, setScore] = useState(null);
    const [showResults, setShowResults] = useState(false);

    // Fetch the quiz details including questions
    useEffect(() => {
        fetch(`/learning-paths/${pathId}/quiz/${quizId}`)
            .then(res => res.json())
            .then(data => setQuiz(data))
            .catch(error => console.error('Error fetching quiz details:', error));
    }, [pathId, quizId]);

    if (!quiz) return <p>Loading quiz...</p>;

    // Handle answer selection for multiple-choice questions
    const handleAnswerChange = (questionId, answer) => {
        setAnswers(prevAnswers => ({
            ...prevAnswers,
            [questionId]: answer,
        }));
    };

    // Submit quiz answers to the backend for scoring
    const handleSubmit = () => {
        fetch(`/learning-paths/${pathId}/quiz/${quizId}/submit`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ answers }),
        })
            .then(res => res.json())
            .then(data => {
                setScore(data.score);
                setShowResults(true);
            })
            .catch(error => console.error('Error submitting quiz:', error));
    };

    return (
        <div>
            <h2>{quiz.title}</h2>
            <p>{quiz.description}</p>
            
            {quiz.questions.map((question, index) => (
                <div key={question.id} style={{ marginBottom: '20px' }}>
                    <h4>Question {index + 1}: {question.text}</h4>

                    {/* Render multiple choice options if available */}
                    {question.choices ? (
                        question.choices.map(choice => (
                            <label key={choice}>
                                <input
                                    type="radio"
                                    name={`question-${question.id}`}
                                    value={choice}
                                    checked={answers[question.id] === choice}
                                    onChange={() => handleAnswerChange(question.id, choice)}
                                />
                                {choice}
                            </label>
                        ))
                    ) : (
                        // Render an input for open-ended questions
                        <input
                            type="text"
                            placeholder="Type your answer here"
                            value={answers[question.id] || ''}
                            onChange={(e) => handleAnswerChange(question.id, e.target.value)}
                        />
                    )}
                </div>
            ))}

            {/* Submit Button */}
            <button onClick={handleSubmit}>Submit Quiz</button>

            {/* Show Results after submission */}
            {showResults && (
                <div>
                    <h3>Quiz Results</h3>
                    <p>Your score: {score} / {quiz.questions.length}</p>
                    {/* Optionally show feedback here */}
                </div>
            )}
        </div>
    );
};

export default QuizDetail;
