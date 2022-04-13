from os import environ
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL').replace('postgres://', 'postgresql://', 1)
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = environ.get('SECRET_KEY')