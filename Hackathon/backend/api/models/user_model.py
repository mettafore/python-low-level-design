from pydantic import BaseModel, EmailStr, SecretStr
from abc import ABC, abstractmethod
from enum import Enum


class Role(Enum):
    """
    Represents the role of a user.
    """
    SELLER = 'seller'
    BUYER = 'buyer'
    ADMIN = 'admin'
    SUPERADMIN = 'superadmin'


class UserCreate(BaseModel, ABC):
    """
    Represents a user creation request.
    """
    email: EmailStr
    password: SecretStr
    first_name: str
    last_name: str
    role: Role  # Fix the role type

    @abstractmethod
    def get_role(self):
        pass


class AdminCreate(UserCreate):
    """
    Represents an admin user creation request.
    """
    role: Role = Role.ADMIN  # You can also give a default value to role in each subclass

    def get_role(self):
        return self.role


class BuyerCreate(UserCreate):
    """
    Represents a buyer user creation request.
    """
    role: Role = Role.BUYER

    def get_role(self):
        return self.role


class SellerCreate(UserCreate):
    """
    Represents a seller user creation request.
    """
    role: Role = Role.SELLER

    def get_role(self):
        return self.role
