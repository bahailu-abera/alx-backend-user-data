#!/usr/bin/env python3
"""
Authentication Module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Authentication module for the api.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if the end point is required to authenticate.
        """
        if not path or not excluded_paths:
            return True

        path_with_slash = path if path.endswith('/') else path + '/'

        if path_with_slash in excluded_paths:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns the Authorization header.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current active user.
        """
        return None
