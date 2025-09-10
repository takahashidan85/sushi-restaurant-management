import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.app_factory import create_app
from app.core.config import Config

@pytest.fixture
def client():
    app = create_app(Config)
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        yield client
