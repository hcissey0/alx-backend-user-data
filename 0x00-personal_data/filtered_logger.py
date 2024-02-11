#!/usr/bin/env python3
"""This is a filtered logger"""

import re


def filter_datum(fields, redaction, message, separator):
    """this will do the work"""
    regex = re.compile(r'(' + '|'.join(fields) + r')=[^{}]+'.format(
        separator))
    return regex.sub(
            lambda match: match.group().split('=')[0] + '=' + redaction, message)
