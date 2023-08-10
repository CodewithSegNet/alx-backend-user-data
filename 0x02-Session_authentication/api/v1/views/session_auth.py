#!/usr/bin/env python3
""" Handling all route for the Session authentication
"""
from flask import Flask, request, jsonify
from api.v1.views import app_views
from models.user import User
from api.v1.app import authi

app_views = Flask(__name__)

"""Create a new route for session authentication login
"""
@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login():
    """Retrieve email and password parameters from request form
    """
    email = request.form.get('email')
    password = request.form.get('password')

    """Check if email or password is missing
    """
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    """Search for a user based on the provided email
    """
    user = User.search({'email': email})
    
    """Check if user was found
    """
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    
    """Check if the provided password is valid for the user
    """
    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    """Create a session ID for the user
    """
    session_id = auth.create_session(user[0].id)
    
    """Convert user details to a dictionary
    """
    user_dict = user[0].to_json()

    """Create the response with user details and set the session cookie
    """
    response = jsonify(user_dict)
    response.set_cookie(app.config['SESSION_NAME'], session_id)

    return response
