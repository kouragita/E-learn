import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False').lower() == 'true'