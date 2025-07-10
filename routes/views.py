from flask import Blueprint, render_template, current_app

views_bp = Blueprint('views', __name__)


@views_bp.route('/')
def index():
    kakao_key = current_app.config['KAKAO_MAP_KEY']
    return render_template('index.html', kakao_key=kakao_key)
