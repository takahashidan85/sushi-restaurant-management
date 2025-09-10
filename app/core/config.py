import os
import psycopg2

class Config:
    """Base configuration."""
    DEBUG = True
    TESTING = False
    ENV = "base"

    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")

    @staticmethod
    def get_postgres_url():
        return (
            f"postgresql+psycopg2://{os.getenv('DB_USER', 'postgres')}:"
            f"{os.getenv('DB_PASSWORD', 'postgres')}@"
            f"{os.getenv('DB_HOST', 'db')}:"
            f"{os.getenv('DB_PORT', '5432')}/"
            f"{os.getenv('DB_NAME', 'sushi_db')}"
        )

    # Ưu tiên DATABASE_URL nếu có
    db_url = os.getenv("DATABASE_URL")

    if db_url:
        SQLALCHEMY_DATABASE_URI = db_url
    else:
        # Thử Postgres
        try:
            conn = psycopg2.connect(
                dbname=os.getenv("DB_NAME", "sushi_db"),
                user=os.getenv("DB_USER", "postgres"),
                password=os.getenv("DB_PASSWORD", "postgres"),
                host=os.getenv("DB_HOST", "db"),
                port=os.getenv("DB_PORT", "5432"),
            )
            conn.close()
            SQLALCHEMY_DATABASE_URI = get_postgres_url()
        except Exception:
            # Fallback SQLite
            SQLALCHEMY_DATABASE_URI = "sqlite:///sushi.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    APP_NAME = os.getenv("APP_NAME", "Sushi Restaurant API")
    APP_PORT = int(os.getenv("APP_PORT", 5000))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"


class ProductionConfig(Config):
    DEBUG = False
    ENV = "production"


class TestingConfig(Config):
    TESTING = True
    ENV = "testing"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
