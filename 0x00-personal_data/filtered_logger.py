#!/usr/bin/env python3
"""This is a filtered logger"""

import re


def filter_datum(fields, redaction, message, separator):
    """this will do the work"""
    [(m := re.sub(f"{f}=[^;]*", f"{f}={redaction}", message) for f in fields]
    return message
