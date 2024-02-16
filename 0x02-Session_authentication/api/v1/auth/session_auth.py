#!/usr/bin/env python3
"""This is the session auth class"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """

    Args:
        Auth (_type_): _description_
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """_summary_

        Args:
            user_id (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
