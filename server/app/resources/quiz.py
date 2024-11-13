from flask_restful import Resource, reqparse
from app.models import db
from app.models.quiz import Quiz
from app.schemas.quiz_schema import QuizSchema

quiz_schema = QuizSchema()
quizzes_schema = QuizSchema(many=True)

class QuizResource(Resource):
    def get(self, quiz_id):
        quiz = Quiz.query.get_or_404(quiz_id)
        return quiz_schema.dump(quiz), 200

    def put(self, quiz_id):
        quiz = Quiz.query.get_or_404(quiz_id)
        parser = reqparse.RequestParser()
        parser.add_argument('question', type=str, required=True)
        parser.add_argument('options', type=list, location='json', required=True)
        parser.add_argument('correct_answer', type=str, required=True)
        args = parser.parse_args()

        quiz.question = args['question']
        quiz.options = args['options']
        quiz.correct_answer = args['correct_answer']
        db.session.commit()
        return quiz_schema.dump(quiz), 200

    def delete(self, quiz_id):
        quiz = Quiz.query.get_or_404(quiz_id)
        db.session.delete(quiz)
        db.session.commit()
        return {'message': 'Quiz deleted'}, 204

class QuizListResource(Resource):
    def get(self):
        quizzes = Quiz.query.all()
        return quizzes_schema.dump(quizzes), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('question', type=str, required=True)
        parser.add_argument('options', type=list, location='json', required=True)
        parser.add_argument('correct_answer', type=str, required=True)
        args = parser.parse_args()

        quiz = Quiz(
            question=args['question'],
            options=args['options'],
            correct_answer=args['correct_answer']
        )
        db.session.add(quiz)
        db.session.commit()
        return quiz_schema.dump(quiz), 201
