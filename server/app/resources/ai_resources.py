from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.ai.ai_service import AIService

class RecommendationsResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        try:
            service = AIService()
            recommendations = service.get_recommendations(user_id)
            return recommendations, 200
        except Exception as e:
            return {"message": f"Failed to generate recommendations: {str(e)}"}, 500
