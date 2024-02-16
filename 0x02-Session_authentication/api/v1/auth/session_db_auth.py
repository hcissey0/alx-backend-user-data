#!/usr/bin/env python3

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
import uuid


class SessionDBAuth(SessionExpAuth):
    """_summary_

    Args:
        SessionExpAuth (_type_): _description_
    """

    def create_session(self, user_id: str = None) -> str:
        """_summary_

        Args:
            user_id (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        session_id = super().create_session(user_id)
        user_session = UserSession(session_id=session_id, user_id=user_id)
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """_summary_

        Args:
            session_id (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        user_sessions = UserSession.search({"session_id": session_id})
        if not user_sessions or user_sessions == []:
            return None
        for user_session in user_sessions:
            if user_session.session_id == session_id:
                return user_session.user_id
        return None

    def destroy_session(self, request=None):
        """

        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_sessions = UserSession.search({"session_id": session_id})
        if not user_sessions or user_sessions == []:
            return None
        for user_session in user_sessions:
            if user_session.session_id == session_id:
                user_session.remove()
                return True

        return False
