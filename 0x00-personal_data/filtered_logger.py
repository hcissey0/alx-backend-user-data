#!/usr/bin/env python3
"""This is a filtered logger"""

import re


def filter_datum(fields, redaction, message, separator):
    """this will do the work"""
    for field in fields:
        message = re.sub(f"{field}=[^;]*", f"{field}={redaction}", message)
    return message
