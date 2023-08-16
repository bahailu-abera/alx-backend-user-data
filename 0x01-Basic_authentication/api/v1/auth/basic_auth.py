#!/usr/bin/env python3
"""
Basic Auth module.
"""
from auth import Auth


class BasicAuth(Auth):
    """
    Basic Auth method
    """
    def __init__(self) -> None:
        super().__init__()
