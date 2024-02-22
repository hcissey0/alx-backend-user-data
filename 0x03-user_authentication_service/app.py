#!/usr/bin/env python3
"""This is the flask app file"""

from flask import Flask, jsonify, request, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def home() -> str:
    """This is the home route"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def users() -> str:
    """This is the function that implements POST /users"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login() -> str:
    """This is the sesion login function

    Returns:
        str: _description_
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email=email)
    res = jsonify({"email": f"{email}", "message": "logged in"})
    res.set_cookie('session_id', session_id)
    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
