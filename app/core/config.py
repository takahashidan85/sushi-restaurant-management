import os

class Config:
    """Base configuration."""
    DEBUG = True
    TESTING = False
    ENV = "base"
    SECRET_KEY = os.environ.get("SECRET_KEY" or "supersecretkey")

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///sushi.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DEV_DATABASE_URL",
        "sqlite:///sushi_dev.db"
    )

class ProductionConfig(Config):
    DEBUG = False
    ENV = "production"

class TestingConfig(Config):
    TESTING = True
    ENV = "testing"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"