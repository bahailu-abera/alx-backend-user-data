#!/usr/bin/env python3
from os import getenv
from flask import jsonify, request
from api.v1.views import app_views


@app_views.route('/auth_session/login', methods=['GET'], strict_slashes=False)
def login():
    """
    Authenticate a user for login.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({ "error": "email missing" }), 400

    if not password:
        return jsonify({ "error": "password missing" }), 400

    from models.user import User

    users = User.search({'email' : email})

    if not users:
        return jsonify({ "error": "no user found for this email" }), 404

    user = users[0]

    if not user.is_valid_password(password):
        return jsonify({ "error": "wrong password" }), 401

    from api.v1.app import auth

    session_id = auth.create_session(user.user_id)

    response = jsonify(user)

    cookie_name = getenv('SESSION_NAME')

    response.set_cookie(cookie_name, session_id)

    return response
