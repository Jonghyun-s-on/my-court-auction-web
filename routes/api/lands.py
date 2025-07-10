from flask import Blueprint, jsonify

lands_bp = Blueprint('lands', __name__)


@lands_bp.route('/lands', methods=['GET'])
def get_lands():
    temp_lands_info = {"id": 1, "no": "A153", "name": "토지 A", "lat": 37.655943, "lng": 126.840551}
    return jsonify(temp_lands_info)
