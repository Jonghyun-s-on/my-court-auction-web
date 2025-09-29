from flask import Flask
from dotenv import load_dotenv
import os

from routes.web.views import views_bp
from routes.api.users import users_bp
from routes.api.lands import lands_bp

# .env 파일 로드
load_dotenv()

app = Flask(__name__)

# get Kakao Map API Key from .env
app.config['KAKAO_MAP_KEY'] = os.getenv("KAKAO_MAP_KEY")

app.register_blueprint(views_bp)
app.register_blueprint(lands_bp, url_prefix='/api')
app.register_blueprint(users_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
