from flask import Blueprint, jsonify
from repository.user_repository import UserRepository

users_bp = Blueprint('users', __name__)


@users_bp.route('/users', methods=['GET'])
def get_lands(startDate, endDate):
    users = UserRepository.get_all(startDate, endDate)

    return jsonify([u.to_dict() for u in users])

@users_bp.route('/users/num', methods=['GET'])
def get_landss():

    return jsonify(a)
