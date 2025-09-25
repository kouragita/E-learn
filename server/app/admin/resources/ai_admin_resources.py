from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from app.models import Resource as ResourceModel
from app.ai.groq_client import GroqClient
from app.ai.prompt_templates import CONTENT_REVIEW_PROMPT

class AdminContentReviewResource(Resource):
    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('resource_id', type=int, required=True, help='Resource ID cannot be blank')
        data = parser.parse_args()

        resource = ResourceModel.query.get(data['resource_id'])
        if not resource or not resource.description:
            return {"message": "Resource not found or has no content to review."}, 404

        prompt = CONTENT_REVIEW_PROMPT.format(content=resource.description)

        try:
            groq_client = GroqClient()
            review = groq_client.generate(prompt)

            if not review:
                return {"error": "Failed to get review from AI service."}, 500

            return {"review": review}, 200
        except Exception as e:
            return {"error": str(e)}, 500
