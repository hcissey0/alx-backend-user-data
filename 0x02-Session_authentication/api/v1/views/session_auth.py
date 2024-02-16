#!/usr/bin/env python3
"""the session auth routes"""

from api.v1.views import app_views
from flask import request, jsonify
from models.user import User
import os


@app_views.route('/auth_session/login',
                 methods=['POST'], strict_slashes=False)
def auth_session_login() -> str:
    """_summary_
    """
    email = request.form.get('email', None)
    if email is None or email == '':
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password', None)
    if password is None or password == '':
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users or users == []:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            out = jsonify(user.to_json())
            out.set_cookie(os.getenv("SESSION_NAME"), session_id)
            return out
    return jsonify({"error": "wrong password"}), 401
