from flask import request, jsonify
from flask_restful import Resource
from app.models import db
from app.models.achievement import Achievement
from app.schemas.achievement_schema import AchievementSchema

achievement_schema = AchievementSchema()
achievements_schema = AchievementSchema(many=True)

class AchievementResource(Resource):
    def get(self, id):
        achievement = Achievement.query.get_or_404(id)
        return achievement_schema.dump(achievement), 200

    def put(self, id):
        data = request.get_json()
        achievement = Achievement.query.get_or_404(id)
        achievement.user_id = data.get("user_id", achievement.user_id)
        achievement.badge_id = data.get("badge_id", achievement.badge_id)
        achievement.date_achieved = data.get("date_achieved", achievement.date_achieved)
        db.session.commit()
        return achievement_schema.dump(achievement), 200

    def delete(self, id):
        achievement = Achievement.query.get_or_404(id)
        db.session.delete(achievement)
        db.session.commit()
        return {"message": "Achievement deleted"}, 204

class AchievementListResource(Resource):
    def get(self):
        achievements = Achievement.query.all()
        return achievements_schema.dump(achievements), 200

    def post(self):
        data = request.get_json()
        new_achievement = Achievement(
            user_id=data["user_id"],
            badge_id=data["badge_id"],
            date_achieved=data["date_achieved"]
        )
        db.session.add(new_achievement)
        db.session.commit()
        return achievement_schema.dump(new_achievement), 201
