import pytest
import sys
import os

# Allow importing from the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from models import db, Plant

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            plant = Plant(name="Test Plant", image="test.jpg", price=9.99)
            db.session.add(plant)
            db.session.flush()  # Get plant.id before commit
            client.plant_id = plant.id
            db.session.commit()
        yield client

def test_patch_plant(client):
    response = client.patch(f'/plants/{client.plant_id}', json={"is_in_stock": False})
    assert response.status_code == 200
    assert response.get_json()["is_in_stock"] is False

def test_delete_plant(client):
    response = client.delete(f'/plants/{client.plant_id}')
    assert response.status_code == 204
