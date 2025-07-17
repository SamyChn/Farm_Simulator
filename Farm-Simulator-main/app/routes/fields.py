from flask import Blueprint, jsonify, request
from datetime import datetime

fields_bp = Blueprint('fields', __name__)

fields = [
    {"id": 1, "name": "Champ A", "crop_type": "aucune", "state": "vide", "last_action": str(datetime.utcnow())},
    {"id": 2, "name": "Champ B", "crop_type": "blé", "state": "semé", "last_action": str(datetime.utcnow())},
    {"id": 3, "name": "Champ C", "crop_type": "maïs", "state": "récolté", "last_action": str(datetime.utcnow())}
]

@fields_bp.route('/fields', methods=['GET'])
def get_fields():
    return jsonify(fields)

@fields_bp.route('/fields/<int:field_id>/plant', methods=['POST'])
def plant_crop(field_id):
    crop = request.args.get('crop', 'blé')
    for field in fields:
        if field['id'] == field_id:
            field['state'] = "semé"
            field['crop_type'] = crop
            field['last_action'] = str(datetime.utcnow())
            return jsonify(field), 200
    return jsonify({"error": "Champ non trouvé"}), 404

@fields_bp.route('/fields/<int:field_id>/harvest', methods=['POST'])
def harvest_crop(field_id):
    for field in fields:
        if field['id'] == field_id:
            field['state'] = "récolté"
            field['last_action'] = str(datetime.utcnow())
            return jsonify(field), 200
    return jsonify({"error": "Champ non trouvé"}), 404

@fields_bp.route('/fields/<int:field_id>/reset', methods=['POST'])
def reset_field(field_id):
    for field in fields:
        if field['id'] == field_id:
            field['state'] = "vide"
            field['crop_type'] = "aucune"
            field['last_action'] = str(datetime.utcnow())
            return jsonify(field), 200
    return jsonify({"error": "Champ non trouvé"}), 404
