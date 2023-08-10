#!/usr/bin/env python3
""" a class that inherits from Auth"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ class attr to store user_id by session_id
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create a Session ID for a user_id.

        Args:
            user_id (str): User ID
        Returns:
            str: Session ID.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Retrieve User ID based on a Session ID

        Args:
            session_id (str): Session ID.

        Returns:
            str: User ID associated with the Session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None):
        """ Return a User instance based on a cookie value.

        Args:
            request: The Flask request object.

        Returns:
            User: The User instance associated with the cookie _my_session
        """
        if request is None:
            return None

        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        return User.ger(user_id)


if __name__ == '__main__':
    session_auth = SessionAuth()
    print(isinstance(session_auth, Auth))
