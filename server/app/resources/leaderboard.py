from flask_restful import Resource
from sqlalchemy import func
from app.models import db
from app.models.user import User
from app.models.badge import Badge
from app.models.achievement import Achievement  # Assuming you track badge achievements here
from app.models.user_profile import UserProfile


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
                UserProfile.avatar_url.label('avatar_url'),
                func.coalesce(func.sum(Badge.points_required), 0).label('total_points'),
                func.array_agg(Badge.name).label('badges_earned')
            )
            .join(Achievement, Achievement.user_id == User.id)  # Join on achievements
            .join(Badge, Achievement.badge_id == Badge.id)  # Join on badges
            .join(UserProfile, UserProfile.user_id == User.id)  # Join on user_profiles
            .group_by(User.id, UserProfile.avatar_url)
            .order_by(func.coalesce(func.sum(Badge.points_required), 0).desc())
            .all()
        )

        # Format the leaderboard response
        leaderboard = [
            {
                "user_id": user.user_id,
                "username": user.username,
                "avatar_url": user.avatar_url,
                "total_points": user.total_points,
                "badges": user.badges_earned
            }
            for user in leaderboard_query
        ]

        return {"leaderboard": leaderboard}, 200
