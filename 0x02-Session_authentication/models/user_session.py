#!/usr/bin/env python3
"""The user sessoion classs"""

from models.base import Base


class UserSession(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """

    def __init__(self, *args: list, **kwargs: dict):
        """ Initialize a User instance
        """
        super().__init__(*args, **kwargs)
        self.user_id = str(kwargs.get('user_id'))
        self.session_id = str(kwargs.get('session_id'))
