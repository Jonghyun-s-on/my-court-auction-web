# 웹 브라우저 주소창을 통해 요청이 왔을 때, 해당 화면(HTML)을 응답해주는 역할
from flask import Blueprint, render_template, current_app

views_bp = Blueprint('views', __name__)

@views_bp.route('/index')
def index():
    kakao_key = current_app.config['KAKAO_MAP_KEY']
    return render_template('index.html', kakao_key=kakao_key)

# 테스트 페이지
# 추후 삭제 예정
@views_bp.route('/test')
def test():
    return render_template('test.html')

# 테스트 페이지
# 추후 삭제 예정
@views_bp.route('/test-test')
def test1():
    return render_template('test2.html')