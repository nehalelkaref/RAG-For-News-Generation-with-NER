from flask import Flask, Blueprint
from flask_cors import CORS

import os

bp = Blueprint('api', __name__)

def create_app():
    app = Flask(__name__)
    
    # if os.environ.get('FLASK_ENV')=='development':
    CORS(app)
    from app.api.routes import bp
    app.register_blueprint(bp) 

    return app