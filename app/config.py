import os

class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "supersecretkey"

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///sushi.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
