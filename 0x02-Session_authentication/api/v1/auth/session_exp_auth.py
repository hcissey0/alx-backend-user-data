#!/usr/bin/env python3
"""The session expiry class"""

from api.v1.auth.session_auth import SessionAuth
import datetime
import os


class SessionExpAuth(SessionAuth):
    """_summary_

    Args:
        SessionAuth (_type_): _description_
    """

    def __init__(self):
        """_summary_
        """
        try:
            self.session_duration = int(os.getenv("SESSION_DURATION"))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id: str = None) -> str:
        """_summary_

        Args:
            user_id (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """_summary_

        Args:
            session_id (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        if session_id is None:
            return None
        session_dictionary = self.user_id_by_session_id.get(session_id)
        if session_dictionary is None:
            return None
        if self.session_duration <= 0:
            return session_dictionary.get('user_id')
        created_at = session_dictionary.get('created_at')
        if created_at is None:
            return None
        expiration = created_at + datetime.timedelta(
                                    seconds=self.session_duration)
        if expiration < datetime.datetime.now():
            return None
        return session_dictionary.get('user_id')
