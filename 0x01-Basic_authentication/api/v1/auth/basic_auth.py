#!/usr/bin/env python3
"""The basic auth class"""

from api.v1.auth.auth import Auth
import base64


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
        tok = authorization_header.split(' ')[-1]
        return tok

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """_summary_

        Args:
            base64_authorization_header (str): _description_

        Returns:
            str: _description_
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded = base64.b64decode(encoded)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """_summary_

        Args:
            self (_type_): _description_
            str (_type_): _description_
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(":")
        return email, password
