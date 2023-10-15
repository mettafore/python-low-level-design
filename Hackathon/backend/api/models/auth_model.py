from abc import ABC, abstractmethod
from pydantic import BaseModel, EmailStr, SecretStr


class AuthRequest(BaseModel, ABC):
    email: EmailStr
    password: SecretStr

class PasswordAuthRequest(AuthRequest):
    pass

class AuthRequestFactory:
    @staticmethod
    def create_auth_request(auth_type: str) -> AuthRequest:
        if auth_type == 'password':
            return PasswordAuthRequest()
        elif auth_type == 'otp':
            return OTPAuthRequest()
        else:
            raise ValueError("Invalid auth type")

class CustomMessageResponse(BaseModel):
    """A generic response model with a message attribute."""

    message: str = "Data created"

class InsertRecordResponse(CustomMessageResponse):
    """A response model for inserting a record."""

    id: int

class TokenResponse(BaseModel):
    token: str
    refresh_token: str

