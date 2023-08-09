#!/usr/bin/env python3
"""
Module for encrypting password
"""
import bcrypt


def hash_password(password) -> str:
    """
    Returns a salted, hashed password, which is a byte string.
    """
    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password
