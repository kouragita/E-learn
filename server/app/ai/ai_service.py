from .groq_client import GroqClient
from .prompt_templates import PromptTemplates
from app.models import LearningPath, User, Progress
from app import db
import json

class AIService:
    def __init__(self):
        self.client = GroqClient()

    def get_recommendations(self, user_id):
        user = User.query.get(user_id)
        if not user:
            raise ValueError("User not found.")

        # Gather user progress
        completed_paths_query = db.session.query(LearningPath.title).join(Progress).filter(Progress.user_id == user_id, Progress.completed == True).all()
        completed_paths = [path.title for path in completed_paths_query]

        # Gather available paths
        available_paths_query = LearningPath.query.filter(LearningPath.id.notin_([p.id for p in user.learning_paths])).all()
        available_paths = [
            {"id": path.id, "title": path.title, "description": path.description, "category": path.category}
            for path in available_paths_query
        ]

        if not available_paths:
            return [] # Return empty list if no paths are available to recommend

        prompt = PromptTemplates.RECOMMEND_PATHS.format(
            completed_paths=json.dumps(completed_paths, indent=2),
            available_paths=json.dumps(available_paths, indent=2)
        )

        response_str = self.client.execute(prompt)
        return json.loads(response_str)

    def generate_quiz(self, content, num_questions=5):
        prompt = PromptTemplates.GENERATE_QUIZ.format(
            num_questions=num_questions,
            content=content
        )
        response_str = self.client.execute(prompt)
        return json.loads(response_str)
