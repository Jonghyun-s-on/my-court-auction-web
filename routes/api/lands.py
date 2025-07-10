from flask import Blueprint, jsonify

lands_bp = Blueprint('lands', __name__)

lands = [
    {"id": 1, "name": "토지 A", "lat": 37.655943, "lng": 126.840551},
    {"id": 2, "name": "토지 B", "lat": 37.654321, "lng": 126.841111},
    {"id": 3, "name": "토지 C", "lat": 37.656789, "lng": 126.842222}
]


@lands_bp.route('/lands')
def get_lands():
    return jsonify(lands)
