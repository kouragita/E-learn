from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User, UserProfile
from .role import Role
from .learning_path import LearningPath, Module, UserLearningPath
from .resource import Resource, Comment, Rating
from .quiz import Quiz
from .badge import Badge, Achievement
from .progress import Progress