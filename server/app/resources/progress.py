from flask_restful import Resource, reqparse
from app.models import db
from app.models import Progress
from app.schemas.progress_schema import ProgressSchema

progress_schema = ProgressSchema()
progresses_schema = ProgressSchema(many=True)

class ProgressResource(Resource):
    def get(self, progress_id):
        progress = Progress.query.get_or_404(progress_id)
        return progress_schema.dump(progress), 200

    def put(self, progress_id):
        progress = Progress.query.get_or_404(progress_id)
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True)
        parser.add_argument('module_id', type=int, required=True)
        parser.add_argument('completed', type=bool, required=True)
        parser.add_argument('completion_date', type=str)
        args = parser.parse_args()

        progress.user_id = args['user_id']
        progress.module_id = args['module_id']
        progress.completed = args['completed']
        progress.completion_date = args.get('completion_date', progress.completion_date)
        db.session.commit()
        return progress_schema.dump(progress), 200

    def delete(self, progress_id):
        progress = Progress.query.get_or_404(progress_id)
        db.session.delete(progress)
        db.session.commit()
        return {'message': 'Progress deleted'}, 204

class ProgressListResource(Resource):
    def get(self):
        progresses = Progress.query.all()
        return progresses_schema.dump(progresses), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True)
        parser.add_argument('module_id', type=int, required=True)
        parser.add_argument('completed', type=bool, required=True)
        parser.add_argument('completion_date', type=str)
        args = parser.parse_args()

        progress = Progress(
            user_id=args['user_id'],
            module_id=args['module_id'],
            completed=args['completed'],
            completion_date=args.get('completion_date')
        )
        db.session.add(progress)
        db.session.commit()
        return progress_schema.dump(progress), 201
