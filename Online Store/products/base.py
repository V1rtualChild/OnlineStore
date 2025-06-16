from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @abstractmethod
    def get_info(self) -> str:
        pass
