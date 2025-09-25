from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import LearningPath, Progress, Module
from app.ai.groq_client import GroqClient
from app.ai.prompt_templates import COURSE_RECOMMENDATION_PROMPT, QUIZ_GENERATION_PROMPT, AI_TUTOR_PROMPT

class RecommendationsResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        
        # Get courses the user has completed
        completed_module_ids = [p.module_id for p in Progress.query.filter_by(user_id=user_id, completed=True).all()]
        completed_path_ids = {m.learning_path_id for m in Module.query.filter(Module.id.in_(completed_module_ids)).all()}
        
        # Get all available courses the user has NOT completed
        available_paths = LearningPath.query.filter(LearningPath.id.notin_(completed_path_ids)).all()
        
        if not available_paths:
            return {"message": "No new courses available for recommendation."}, 200

        completed_courses_titles = [lp.title for lp in LearningPath.query.filter(LearningPath.id.in_(completed_path_ids)).all()]
        available_courses_titles = [lp.title for lp in available_paths]

        prompt = COURSE_RECOMMENDATION_PROMPT.format(
            completed_courses=", ".join(completed_courses_titles) or "None",
            available_courses=", ".join(available_courses_titles)
        )

        try:
            groq_client = GroqClient()
            raw_recommendations = groq_client.generate(prompt)
            
            if not raw_recommendations:
                return {"error": "Failed to get recommendations from AI service."}, 500

            recommended_titles = [title.strip() for title in raw_recommendations.split(',')]
            
            # Match titles back to LearningPath objects
            recommended_courses = [path for path in available_paths if path.title in recommended_titles]
            
            # Serialize the response
            response_data = [{
                'id': course.id,
                'title': course.title,
                'description': course.description,
                'category': course.category
            } for course in recommended_courses]

            return {"recommendations": response_data}, 200
        except Exception as e:
            return {"error": str(e)}, 500

class ContentGenerationResource(Resource):
    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('content', type=str, required=True, help='Content for quiz generation cannot be blank')
        parser.add_argument('num_questions', type=int, default=3)
        data = parser.parse_args()

        prompt = QUIZ_GENERATION_PROMPT.format(
            num_questions=data['num_questions'],
            content=data['content']
        )

        try:
            groq_client = GroqClient()
            generated_content = groq_client.generate(prompt)

            if not generated_content:
                return {"error": "Failed to generate content from AI service."}, 500

            return {"generated_content": generated_content}, 200
        except Exception as e:
            return {"error": str(e)}, 500

class AITutorResource(Resource):
    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('question', type=str, required=True, help='Question cannot be blank')
        parser.add_argument('context', type=str, required=True, help='Context cannot be blank')
        data = parser.parse_args()

        prompt = AI_TUTOR_PROMPT.format(
            context=data['context'],
            question=data['question']
        )

        try:
            groq_client = GroqClient()
            answer = groq_client.generate(prompt)

            if not answer:
                return {"error": "Failed to get an answer from the AI tutor."}, 500

            return {"answer": answer}, 200
        except Exception as e:
            return {"error": str(e)}, 500