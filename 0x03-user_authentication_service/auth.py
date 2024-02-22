#!/usr/bin/env python3
"""This is the auth file"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """The hash password function that hashes the password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
