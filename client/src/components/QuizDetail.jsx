import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const QuizDetail = () => {
    const { pathId, moduleId, quizId } = useParams();
    const [quiz, setQuiz] = useState(null);
    const [answers, setAnswers] = useState({});
    const [score, setScore] = useState(null);
    const [showResults, setShowResults] = useState(false);
    const [error, setError] = useState(null);

    // Fetch the quiz details including questions
    useEffect(() => {
        const fetchQuiz = async () => {
            try {
                const response = await fetch(`/api/learning-paths/${pathId}/modules/${moduleId}/quiz/${quizId}`);
                if (!response.ok) throw new Error(`Failed to fetch quiz: ${response.statusText}`);
                
                const data = await response.json();
                setQuiz(data);
                setAnswers({});
                setScore(null);
                setShowResults(false);
                setError(null);
            } catch (err) {
                console.error('Error fetching quiz details:', err);
                setError('Failed to load quiz. Please try again later.');
            }
        };

        fetchQuiz();
    }, [pathId, moduleId, quizId]);

    if (error) return <p>{error}</p>;
    if (!quiz) return <p>Loading quiz...</p>;

    // Handle answer selection for multiple-choice questions
    const handleAnswerChange = (questionId, answer) => {
        setAnswers((prevAnswers) => ({
            ...prevAnswers,
            [questionId]: answer,
        }));
    };

    // Submit quiz answers to the backend for scoring
    const handleSubmit = async () => {
        try {
            const response = await fetch(`/api/learning-paths/${pathId}/modules/${moduleId}/quiz/${quizId}/submit`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ answers }),
            });
            if (!response.ok) throw new Error(`Failed to submit quiz: ${response.statusText}`);

            const data = await response.json();
            setScore(data.score);
            setShowResults(true);
        } catch (err) {
            console.error('Error submitting quiz:', err);
            setError('Failed to submit answers. Please try again.');
        }
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
                        question.choices.map((choice) => (
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
            {showResults && score !== null && (
                <div>
                    <h3>Quiz Results</h3>
                    <p>Your score: {score} / {quiz.questions.length}</p>
                </div>
            )}
        </div>
    );
};

export default QuizDetail;
