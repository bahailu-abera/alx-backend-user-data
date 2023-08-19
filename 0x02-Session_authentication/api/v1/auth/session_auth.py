#!/usr/bin/env python3
"""
Session Based Authentication.
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """
    Session Based Authentication object.
    """
    user_id_by_session_id = {}

    def __init__(self) -> None:
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = uuid4()

        self.user_id_by_session_id = session_id

        return session_id
