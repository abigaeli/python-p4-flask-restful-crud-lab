from models import db, Plant
from app import app

with app.app_context():
    Plant.query.delete()

    plant1 = Plant(name="Aloe", image="./images/aloe.jpg", price=11.50, is_in_stock=True)
    plant2 = Plant(name="Fiddle Leaf Fig", image="./images/fig.jpg", price=15.75, is_in_stock=True)

    db.session.add_all([plant1, plant2])
    db.session.commit()
    print("Database seeded!")
