from flask_restful import Resource
from sqlalchemy import func
from app.models import db
from app.models.user import User
from app.models.badge import Badge
from app.models.achievement import Achievement  # Assuming you track badge achievements here


class LeaderboardResource(Resource):
    def get(self):
        """
        Fetch a leaderboard showing users with their total points and badges earned.
        The users are sorted by points in descending order.
        """
        leaderboard_query = (
            db.session.query(
                User.id.label('user_id'),
                User.username.label('username'),
                func.coalesce(func.sum(Badge.points_required), 0).label('total_points'),
                func.array_agg(Badge.name).label('badges_earned')
            )
            .join(Achievement, Achievement.user_id == User.id)  # Join on achievements
            .join(Badge, Achievement.badge_id == Badge.id)  # Join on badges
            .group_by(User.id)
            .order_by(func.coalesce(func.sum(Badge.points_required), 0).desc())
            .all()
        )

        # Format the leaderboard response
        leaderboard = [
            {
                "user_id": user.user_id,
                "username": user.username,
                "total_points": user.total_points,
                "badges": user.badges_earned
            }
            for user in leaderboard_query
        ]

        return {"leaderboard": leaderboard}, 200
