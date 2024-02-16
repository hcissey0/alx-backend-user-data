#!/usr/bin/env python3
"""The basic auth class"""

from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


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
        email = decoded_base64_authorization_header.split(":")[0]
        password = ":".join(decoded_base64_authorization_header.split(":")[1:])
        return email, password

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """

        Args:
            self (_type_): _description_
        """
        if user_email is None or user_pwd is None:
            return None
        if type(user_email) is not str or type(user_pwd) is not str:
            return None
        try:
            users = User.search({'email': user_email})
            if not users or users == []:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
            return None
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """_summary_

        Returns:
            _type_: _description_
        """
        header = self.authorization_header(request)
        b64 = self.extract_base64_authorization_header(header)
        decoded = self.decode_base64_authorization_header(b64)
        email, password = self.extract_user_credentials(decoded)
        user = self.user_object_from_credentials(email, password)
        return user
