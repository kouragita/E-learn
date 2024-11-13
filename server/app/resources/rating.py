from flask_restful import Resource, reqparse
from app.models import db
from app.models.rating import Rating
from app.schemas.rating_schema import RatingSchema

rating_schema = RatingSchema()
ratings_schema = RatingSchema(many=True)

class RatingResource(Resource):
    def get(self, rating_id):
        rating = Rating.query.get_or_404(rating_id)
        return rating_schema.dump(rating), 200

    def put(self, rating_id):
        rating = Rating.query.get_or_404(rating_id)
        parser = reqparse.RequestParser()
        parser.add_argument('value', type=int, required=True)
        parser.add_argument('user_id', type=int, required=True)
        parser.add_argument('resource_id', type=int, required=True)
        args = parser.parse_args()

        rating.value = args['value']
        rating.user_id = args['user_id']
        rating.resource_id = args['resource_id']
        db.session.commit()
        return rating_schema.dump(rating), 200

    def delete(self, rating_id):
        rating = Rating.query.get_or_404(rating_id)
        db.session.delete(rating)
        db.session.commit()
        return {'message': 'Rating deleted'}, 204

class RatingListResource(Resource):
    def get(self):
        ratings = Rating.query.all()
        return ratings_schema.dump(ratings), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('value', type=int, required=True)
        parser.add_argument('user_id', type=int, required=True)
        parser.add_argument('resource_id', type=int, required=True)
        args = parser.parse_args()

        rating = Rating(
            value=args['value'],
            user_id=args['user_id'],
            resource_id=args['resource_id']
        )
        db.session.add(rating)
        db.session.commit()
        return rating_schema.dump(rating), 201
