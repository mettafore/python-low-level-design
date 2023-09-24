from abc import ABC, abstractmethod

class Features(ABC):
    pass

class HistoryManager(Features):

    @abstractmethod
    def view_history(self):
        pass
    @abstractmethod
    def append_history(self):
        pass

class InMemoryHistoryManager(HistoryManager):
    def __init__(self):
        self.history = []
    def view_history(self):
        for idx, history in enumerate(self.history):
            print(f"{idx+1}.", history)
        input("Press enter to continue")
    def append_history(self, history):
        self.history.append(history)

class Calculation(Features):
    @abstractmethod
    def calculate(self, x, y):
        pass

class Addition(Calculation):
    def calculate(self, x, y):
        return x + y
    
class Subtraction(Calculation):
    def calculate(self, x, y):
        return x - y
    
class Multiplication(Calculation):
    def calculate(self, x, y):
        return x * y
    
class Division(Calculation):
    def calculate(self, x, y):
        return x / y
    
