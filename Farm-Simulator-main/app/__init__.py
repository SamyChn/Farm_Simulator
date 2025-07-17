import os
from flask import Flask
from flask_cors import CORS
from app.models import db
from app.routes.fields import fields_bp  

def create_app():
    app = Flask(__name__)
    
    
    basedir = os.path.abspath(os.path.dirname(__file__))

    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '../instance/database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

   
    CORS(app)
    db.init_app(app)

    
    app.register_blueprint(fields_bp)

    
    with app.app_context():
        db.create_all()

    return app
