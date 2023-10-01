from abc import ABC, abstractmethod
from models.user_model import Buyer, Seller, Admin

class UserFactory(ABC):
    @abstractmethod
    def create_user(self):
        pass

class BuyerFactory(UserFactory):
    def create_user(self):
        return Buyer()

class SellerFactory(UserFactory):
    def create_user(self):
        return Seller()

class AdminFactory(UserFactory):
    def create_user(self):
        return Admin()

class UserFactoryCreator:
    @staticmethod
    def create_factory(factory_type):
        factories = {
            'Buyer': BuyerFactory,
            'Seller': SellerFactory,
            'Admin': AdminFactory
        }
        try:
            return factories[factory_type]()
        except KeyError:
            raise ValueError("Invalid factory type")


