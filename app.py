from flask import Flask, make_response, request, jsonify
from flask_cors import CORS # this allows cross-origin requests
from flask_security import Security
from flask_restful import Api

# We will create authentication and CRUD APIs using Flask RESTful and Flask-Security .
# We would implement authentication token mechanism using Flask-Security .

from config import Config
from database import db
from user_datastore import user_datastore

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Security(app, user_datastore)

    api = Api(app)

    return app, api

def init_db(app):
    with app.app_context():
        db.create_all()

        admin_role = user_datastore.find_or_create_role(name='admin', description = 'Admin Role')
        user_role = user_datastore.find_or_create_role(name='user', description = 'User Role')

        admin_user = user_datastore.find_user(username='admin')
        if not admin_user:
            user_datastore.create_user(
                username = "admin",
                email = "admin@gmail.com",
                password = "admin123",
                roles = [admin_role, user_role]
            )

        db.session.commit()
        print("Database created and initial data added.")

app, api = create_app()
CORS(app) # Enable CORS for the app

if __name__ == "__main__":
    init_db(app) # Initialize the database and create default roles and users .
    app.run(debug=True)