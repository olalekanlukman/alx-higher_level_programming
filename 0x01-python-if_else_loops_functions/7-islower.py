#!/usr/bin/python3
# 7-islower.py
# Lukman Mohammed

def islower(c):
    """Check for lowercase characters."""
    if c >= chr(97) and c <= chr(122):
        return True
    else:
        return False
