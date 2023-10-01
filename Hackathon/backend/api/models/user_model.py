from pydantic import BaseModel, EmailStr, SecretStr
from abc import ABC, abstractmethod

class User(BaseModel, ABC):
    id: int
    name: str
    email: EmailStr
    password: SecretStr
    role: str  

    @abstractmethod
    def get_role(self):
        pass

class Admin(User):
    role: str = 'admin'  # You can also give a default value to role in each subclass

    def get_role(self):
        return self.role

class Buyer(User):
    role: str = 'buyer'

    def get_role(self):
        return self.role

class Seller(User):
    role: str = 'seller'

    def get_role(self):
        return self.role

