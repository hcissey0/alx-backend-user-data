#!/usr/bin/env python3
"""This is the main testing file"""

import requests


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

BASE_URL = 'http://localhost:5000'


def register_user(email: str, password: str) -> None:
    """This is used to test the register user

    Args:
        email (str): The email
        password (str): The password
    """
    url = f"{BASE_URL}/users"
    data = {"email": email, "password": password}
    res = requests.post(url, data=data)
    assert res.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    """Testing logging in with a wrong password

    Args:
        email (str): The email
        password (str): The wrong password
    """
    url = f"{BASE_URL}/users"
    data = {"email": email, "password": password}
    res = requests.post(url, data=data)
    assert res.status_code == 400


def log_in(email: str, password: str) -> str:
    """This is used to login

    Args:
        email (str): The email
        password (str): The password

    Returns:
        str: The session id
    """
    url = f"{BASE_URL}/sessions"
    data = {"email": email, "password": password}
    res = requests.post(url, data=data)
    assert res.status_code == 200
    session_id = res.cookies.get('session_id')
    return session_id


def profile_unlogged() -> None:
    """Checks if the profile is logged or not
    """
    url = f"{BASE_URL}/profile"
    res = requests.get(url)
    assert res.status_code == 403


def profile_logged(session_id: str) -> None:
    """Checks if the profile is logged

    Args:
        session_id (str): The session id
    """
    url = f"{BASE_URL}/profile"
    data = {"session_id": session_id}
    res = requests.get(url, cookies=data)
    assert res.status_code == 200


def log_out(session_id: str) -> None:
    """This is to test the logout

    Args:
        session_id (str): The session id
    """
    url = f"{BASE_URL}/sessions"
    data = {"session_id": session_id}
    res = requests.delete(url, cookies=data)
    assert res.status_code == 200


def reset_password_token(email: str) -> str:
    """used to get the reset password token

    Args:
        email (str): The email

    Returns:
        str: The reset password token
    """
    url = f"{BASE_URL}/reset_password"
    data = {"email": email}
    res = requests.post(url, data=data)
    assert res.status_code == 200
    return res.json()['reset_token']


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Testin the updating password

    Args:
        email (str): The email
        reset_token (str): The reset password token
        new_password (str): The new password
    """
    url = f"{BASE_URL}/reset_password"
    data = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password
    }
    res = requests.put(url, data=data)
    assert res.status_code == 200


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
