#!/usr/bin/env python3
"""
Auth
"""
import bcrypt

from db import DB, User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Encrypts a password.
    """
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user.
        """
        try:
            if self._db.find_user_by(email=email):
                raise ValueError("User {} already exists.".format(email))

        except NoResultFound:
            hashed_pass = _hash_password(password)

            return self._db.add_user(email=email, hashed_password=hashed_pass)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Login validation.
        """
        try:
            user = self._db.find_user_by(email=email)

            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)

        except NoResultFound:
            return False
