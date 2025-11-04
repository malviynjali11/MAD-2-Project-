from flask_restful import Resource
from flask import request, jsonify
from user_datastore import user_datastore

class LoginUser(Resource):
    def post(self):
        login_cred = request.get_json()

        if not login_cred or not login_cred.get('username') or not login_cred.get('password'):
            result = {
                'message': 'Username and password are required.'
            }
            return jsonify(result), 400
        
        username = login_cred['username']
        password = login_cred['password']

        # Data Validation 

        user = user_datastore.find_user(username=username)
        if not user:
            return jsonify({'message' : 'User not found'}), 404
        if not user_datastore.verify_password(password, user.password):
            return jsonify({'message' : 'Invalid password'}), 401