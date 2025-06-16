from .base import Product

class Book(Product):
    def get_info(self):
        return f"Книга: {self.name}, Ціна: {self.price} грн"

class Laptop(Product):
    def get_info(self):
        return f"Ноутбук: {self.name}, Ціна: {self.price} грн"

class TShirt(Product):
    def get_info(self):
        return f"Футболка: {self.name}, Ціна: {self.price} грн"

class ProductFactory:
    @staticmethod
    def create_product(product_type: str, name: str, price: float) -> Product:
        if product_type == "book":
            return Book(name, price)
        elif product_type == "laptop":
            return Laptop(name, price)
        elif product_type == "tshirt":
            return TShirt(name, price)
        else:
            raise ValueError(f"Тип продукту '{product_type}' не підтримується.")
