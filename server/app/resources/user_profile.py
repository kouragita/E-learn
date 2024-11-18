from flask_restful import Resource, reqparse
from app.models import db
from app.models.user_profile import UserProfile
from app.schemas.user_profiles_schema import UserProfileSchema
from flask import jsonify

user_profile_schema = UserProfileSchema()
user_profiles_schema = UserProfileSchema(many=True)

class UserProfileResource(Resource):
    def get(self, user_id):
        profile = UserProfile.query.get(user_id)
        if not profile:
            return {"message": "User profile not found"}, 404
        return user_profile_schema.dump(profile), 200

    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('points', type=int, required=False)
        parser.add_argument('xp', type=int, required=False)
        parser.add_argument('bio', type=str, required=False)
        parser.add_argument('avatar_url', type=str, required=False)
        parser.add_argument('last_active', type=str, required=False)  # Should be handled properly for datetime

        data = parser.parse_args()

        profile = UserProfile.query.get(user_id)
        if not profile:
            return {"message": "User profile not found"}, 404

        # Update fields if provided
        if data['points'] is not None:
            profile.points = data['points']
        if data['xp'] is not None:
            profile.xp = data['xp']
        if data['bio'] is not None:
            profile.bio = data['bio']
        if data['avatar_url'] is not None:
            profile.avatar_url = data['avatar_url']
        if data['last_active'] is not None:
            profile.last_active = data['last_active']  # Ensure this is parsed properly as a datetime

        db.session.commit()
        return user_profile_schema.dump(profile), 200

    def delete(self, user_id):
        profile = UserProfile.query.get(user_id)
        if not profile:
            return {"message": "User profile not found"}, 404

        db.session.delete(profile)
        db.session.commit()
        return {"message": "User profile deleted successfully"}, 200

class UserProfileListResource(Resource):
    def get(self):
        profiles = UserProfile.query.all()
        return user_profiles_schema.dump(profiles), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True)
        parser.add_argument('points', type=int, required=False, default=0)
        parser.add_argument('xp', type=int, required=False, default=0)
        parser.add_argument('bio', type=str, required=False)
        parser.add_argument('avatar_url', type=str, required=False)
        parser.add_argument('last_active', type=str, required=False)

        data = parser.parse_args()

        # Check if the user profile already exists
        if UserProfile.query.get(data['user_id']):
            return {"message": "User profile already exists"}, 409

        new_profile = UserProfile(
            user_id=data['user_id'],
            points=data['points'],
            xp=data['xp'],
            bio=data['bio'],
            avatar_url=data['avatar_url'],
            last_active=data['last_active']  
        )

        db.session.add(new_profile)
        db.session.commit()
        return user_profile_schema.dump(new_profile), 201
