from abc import ABC, abstractmethod
from features import Addition, Subtraction, Multiplication, Division, InMemoryHistoryManager

class FeatureFactory(ABC):
    """An abstract base class for creating calculator factories."""
    @abstractmethod
    def create_feature(self):
        """Creates a calculator."""
        pass

    @staticmethod
    def create_factory(type):
        """Creates a factory for a given feature type."""
        if type == "+":
            return AdditionFactory()
        elif type == "-":
            return SubtractionFactory()
        elif type == "*":
            return MultiplicationFactory()
        elif type == "/":
            return DivisionFactory()
        elif type == "history":
            return InMemoryHistoryManager()
        else:
            raise Exception("Invalid calculation type") from None

    @staticmethod
    def get_available_calculators():
        """Returns a list of available calculator types."""
        return ["+", "-", "*", "/"]


class AdditionFactory(FeatureFactory):
    """A factory for creating addition calculators."""
    def create_feature(self):
        """Creates an addition calculator."""
        return Addition()
    
class SubtractionFactory(FeatureFactory):
    """A factory for creating subtraction calculators."""
    def create_feature(self):
        """Creates a subtraction calculator."""
        return Subtraction()
    
class MultiplicationFactory(FeatureFactory):
    """A factory for creating multiplication calculators."""
    def create_feature(self):
        """Creates a multiplication calculator."""
        return Multiplication()
    
class DivisionFactory(FeatureFactory):
    """A factory for creating division calculators."""
    def create_feature(self):
        """Creates a division calculator."""
        return Division()
    
