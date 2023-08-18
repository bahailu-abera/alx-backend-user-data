#!/usr/bin/env python3
"""
Basic Auth module.
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
    Basic Auth method
    """
    def __init__(self) -> None:
        super().__init__()

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorization
        header for a Basic Authentication
        """
        if authorization_header is None \
           or not isinstance(authorization_header, str) \
           or not authorization_header.startswith('Basic '):
            return None

        return " ".join(authorization_header.split(' ')[1:])

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) -> str:
        """
        Returns the decoded value of a Base64 string base64_authorization_header
        """
        try:
            base64_bytes = base64_authorization_header.encode("utf-8")

            base64_string_bytes = base64.b64decode(base64_bytes)

            return base64_string_bytes.decode("utf-8")

        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Returns the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None or \
           not isinstance(decoded_base64_authorization_header, str) or \
           ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':')

        return email, password
