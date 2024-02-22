#!/usr/bin/env python3
"""This is the auth file"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from typing import Union
import uuid


def _hash_password(password: str) -> bytes:
    """The hash password function that hashes the password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generates a uuid in a string format

    Raises:
        ValueError: _description_

    Returns:
        str: _description_
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """This is used to registe a user"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f'User {email} already exists')
        except NoResultFound:
            pass
        hashed_password = _hash_password(password)
        user = self._db.add_user(email, hashed_password)

        return user

    def valid_login(self, email: str, password: str) -> bool:
        """Checks if email and password are valid

        Args:
            email (str): The email
            password (str): The password

        Returns:
            bool: True if valid otherwise False
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)

    def create_session(self, email: str) -> str:
        """Creates a session and returns the string
        of the session id

        Args:
            email (str): The email

        Returns:
            str: The session id for the created session
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """This is used to get a user by the session id

        Args:
            session_id (str): The session id

        Returns:
            Union[User, None]: The user or None if not found
        """
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destroy_session(self, user_id: int) -> None:
        """Destroys or deletes a user's session

        Args:
            user_id (int): The user id
        """
        try:
            self._db.update_user(user_id, session_id=None)
        except ValueError:
            return
