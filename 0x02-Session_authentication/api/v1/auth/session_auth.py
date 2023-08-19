#!/usr/bin/env python3
"""
Session Based Authentication.
"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    Session Based Authentication object.
    """
    def __init__(self) -> None:
        super().__init__()
