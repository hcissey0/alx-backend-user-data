#!/usr/bin/env python3
"""This is the file for authentication"""

from flask import request
from typing import List, TypeVar


class Auth:
    """This is the auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """_summary_

        Args:
            path (str): _description_
            excluded_paths (List[str]): _description_

        Returns:
            bool: _description_
        """
        if path is None or excluded_paths is None:
            return True

        path = path.rstrip("/")
        for ex_path in excluded_paths:
            if path == ex_path.rstrip("/"):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """_summary_

        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            str:
        """
        if request is None:
            return None
        if request.headers is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """This is the getter for the current user
        """
        return None
