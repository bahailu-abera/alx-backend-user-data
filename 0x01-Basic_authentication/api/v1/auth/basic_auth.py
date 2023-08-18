#!/usr/bin/env python3
"""
Basic Auth module.
"""
from api.v1.auth.auth import Auth
from flask import request


class BasicAuth(Auth):
    """
    Basic Auth method
    """
    def __init__(self) -> None:
        super().__init__()

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorization header for a Basic Authentication
        """
        authorization_header = self.authorization_header(request)

        if authorization_header is None or not isinstance(authorization_header, str) \
            or not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split(' ')[1:]
