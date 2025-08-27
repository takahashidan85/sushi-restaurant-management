import sys, os
from pathlib import Path
repo_root = Path(__file__).resolve().parent.parent
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

import pytest
from app import create_app
from app.extensions import db as _db

@pytest.fixture(scope='function')
def app():
    config = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    }
    app = create_app(test_config=config)
    with app.app_context():
        # create tables using models' define_models to ensure tables exist
        from app.infrastructure import define_models as _dm  # not directly available; we'll import via models module
        try:
            # try to import and define models
            from app.infrastructure.models import define_models
            define_models(_db)
        except Exception:
            pass
        _db.create_all()
        yield app
        _db.session.remove()
        _db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()
