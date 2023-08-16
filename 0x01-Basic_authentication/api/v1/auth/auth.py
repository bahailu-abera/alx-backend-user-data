#!/usr/bin/env python3
"""
Authentication Module
"""
from flask import request
from typing import List


class Auth:
    def __init__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        """
        return None
