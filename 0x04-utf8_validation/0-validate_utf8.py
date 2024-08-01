#!/usr/bin/python3
"""
a method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    checks for a valid UTF-8 encoding
    """
    if not all(0 <= byte <= 255 for byte in data):
        return False
    try:
        bytes(data).decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False
