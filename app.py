from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from models import db
from routes import plant_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)
    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(plant_bp, url_prefix="/plants")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(port=5555)
