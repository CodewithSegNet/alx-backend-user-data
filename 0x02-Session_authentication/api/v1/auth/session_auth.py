#!/usr/bin/env python3
""" a class that inherits from Auth"""
from api.v1.auth.auth import Auth

class SessionAuth(Auth):
    pass

if __name__ == '__main__':
    session_auth = SessionAuth()
    print(isinstance(session_auth, Auth))
