"""
Stores prompt templates for interacting with the Groq LLM.
"""

COURSE_RECOMMENDATION_PROMPT = """
Based on the user's learning history and the available courses, please recommend the top 3 most relevant courses for them to take next.

**User's Completed Courses:**
{completed_courses}

**All Available Courses:**
{available_courses}

Respond with ONLY a comma-separated list of the recommended course titles. For example: Course A, Course B, Course C
"""

AI_TUTOR_PROMPT = """
You are a helpful and encouraging AI Tutor. Given the following context from a lesson the user is currently studying, please answer the user's question clearly and concisely. If the question is outside the provided context, politely state that you can only answer questions related to the lesson material.

**Lesson Context:**
---
{context}
---

**User's Question:** {question}
"""

QUIZ_GENERATION_PROMPT = """
You are an expert instructional designer. Based on the following content, generate a JSON object containing a list of {num_questions} multiple-choice quiz questions. Each question should be an object with "question", a list of "options", and the "correct_answer". Ensure the correct answer is one of the options.

**Content to analyze:**
---
{content}
---

Respond with ONLY the raw JSON object.
"""

CONTENT_REVIEW_PROMPT = """
You are an AI Quality Assurance assistant for an e-learning platform. Review the following content submitted by a contributor. Provide a brief, constructive analysis covering these points:
1.  **Clarity:** Is the explanation clear and easy to understand?
2.  **Accuracy:** Are there any potential factual inaccuracies? (If you are unsure, state that.)
3.  **Engagement:** Is the content engaging? Suggest one way to make it more interactive.

Format your response as a simple JSON object with keys "clarity", "accuracy", and "engagement".

**Content to review:**
---
{content}
---
"""
