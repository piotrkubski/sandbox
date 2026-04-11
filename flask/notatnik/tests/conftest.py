import pytest
from app import create_app
from app.models import db as _db
from app.config import TestingConfig


@pytest.fixture
def client():
    app = create_app(TestingConfig)

    with app.app_context():
        yield app.test_client()
        _db.drop_all()            # czyści bazę po teście