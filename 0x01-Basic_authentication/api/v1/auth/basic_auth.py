#!/usr/bin/env python3
"""The basic auth class"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """_summary_

    Args:
        Auth (_type_): _description_
    """

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """_summary_

        Args:
            authorization_header (str): _description_

        Returns:
            str: _description_
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        authorization_header = authorization_header.strip()
        return authorization_header.removeprefix("Basic ")

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """_summary_

        Args:
            base64_authorization_header (str): _description_

        Returns:
            str: _description_
        """
        pass
