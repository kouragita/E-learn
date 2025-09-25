from flask_restful import Resource, reqparse
import json
from app.models import db
from app.models.quiz import Quiz
from app.schemas.quiz_schema import QuizSchema
from app.auth.decorators import admin_required
# from app.ai.ai_service import AIService

quiz_schema = QuizSchema()
quizzes_schema = QuizSchema(many=True)

# class AIQuizGenerateResource(Resource):
#     method_decorators = [admin_required()]
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('content', type=str, required=True)
#         parser.add_argument('num_questions', type=int, default=5)
#         data = parser.parse_args()
#         try:
#             service = AIService()
#             quiz_data = service.generate_quiz(data['content'], data['num_questions'])
#             return quiz_data, 200
#         except Exception as e:
#             return {"message": f"Failed to generate quiz: {str(e)}"}, 500

class AdminQuizListResource(Resource):
    method_decorators = [admin_required()]

    def get(self, module_id):
        quizzes = Quiz.query.filter_by(module_id=module_id).all()
        return quizzes_schema.dump(quizzes), 200

    def post(self, module_id):
        parser = reqparse.RequestParser()
        parser.add_argument('question', type=str, required=True)
        parser.add_argument('options', type=list, location='json', required=True)
        parser.add_argument('correct_answer', type=str, required=True)
        data = parser.parse_args()

        new_quiz = Quiz(
            module_id=module_id,
            question=data['question'],
            options=json.dumps(data['options']), # Store options as JSON string
            correct_answer=data['correct_answer']
        )
        db.session.add(new_quiz)
        db.session.commit()
        return quiz_schema.dump(new_quiz), 201

class AdminQuizResource(Resource):
    method_decorators = [admin_required()]

    def get(self, quiz_id):
        quiz = Quiz.query.get_or_404(quiz_id)
        return quiz_schema.dump(quiz)

    def put(self, quiz_id):
        quiz = Quiz.query.get_or_404(quiz_id)
        parser = reqparse.RequestParser()
        parser.add_argument('question', type=str)
        parser.add_argument('options', type=list, location='json')
        parser.add_argument('correct_answer', type=str)
        data = parser.parse_args()

        if data.get('question'):
            quiz.question = data['question']
        if data.get('options'):
            quiz.options = json.dumps(data['options'])
        if data.get('correct_answer'):
            quiz.correct_answer = data['correct_answer']
        
        db.session.commit()
        return quiz_schema.dump(quiz)

    def delete(self, quiz_id):
        quiz = Quiz.query.get_or_404(quiz_id)
        db.session.delete(quiz)
        db.session.commit()
        return {'message': 'Quiz deleted'}, 200
