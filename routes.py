from flask import Blueprint, request, jsonify, make_response
from models import db, Plant

plant_bp = Blueprint("plants", __name__)

# PATCH /plants/<id>
@plant_bp.route("/<int:id>", methods=["PATCH"])
def update_plant(id):
    plant = Plant.query.get_or_404(id)
    data = request.get_json()

    if "is_in_stock" in data:
        plant.is_in_stock = data["is_in_stock"]

    db.session.commit()
    return jsonify(plant.to_dict()), 200

# DELETE /plants/<id>
@plant_bp.route("/<int:id>", methods=["DELETE"])
def delete_plant(id):
    plant = Plant.query.get_or_404(id)
    db.session.delete(plant)
    db.session.commit()
    return "", 204
