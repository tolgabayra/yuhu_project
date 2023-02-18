import os


class Config:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = os.getenv("JWT_ACCESS_TOKEN_EXPIRES")
    JWT_TOKEN_LOCATION = ['cookies']
    SESSION_COOKIE_HTTPONLY = True
