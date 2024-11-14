from app import db

from .user import User
from .role import Role
from .user_profile import UserProfile
from .learning_path import LearningPath
from .module import Module
from .resource import Resource
from .quiz import Quiz
from .comment import Comment
from .rating import Rating
from .badge import Badge
from .achievement import Achievement
from .progress import Progress
from .user_learning_path import UserLearningPath

__all__ = [
    'User', 'Role', 'UserProfile', 'LearningPath', 'Module', 'Resource',
    'Quiz', 'Comment', 'Rating', 'Badge', 'Achievement', 'Progress',
    'UserLearningPath'
]
