import os

class Config:
    """Base configuration."""
    DEBUG = True
    TESTING = False
    ENV = "base"

    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///sushi.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    APP_NAME = os.getenv("APP_NAME", "Sushi Restaurant API")
    APP_PORT = int(os.getenv("APP_PORT", 5000))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

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
