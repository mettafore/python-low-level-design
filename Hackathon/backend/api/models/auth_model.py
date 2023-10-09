from pydantic import BaseModel, EmailStr


class AuthRequest(BaseModel):
    email: EmailStr
    password: str

class CustomMessageResponse(BaseModel):
    """A generic response model with a message attribute."""

    message: str = "Data created"

class InsertRecordResponse(CustomMessageResponse):
    """A response model for inserting a record."""

    id: int
