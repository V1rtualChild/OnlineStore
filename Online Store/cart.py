class ShoppingCart:
    _instance = None

    def __init__(self):
        if ShoppingCart._instance is not None:
            raise Exception("Це Singleton клас. Використовуйте get_instance().")
        self.items = []

    @staticmethod
    def get_instance():
        if ShoppingCart._instance is None:
            ShoppingCart._instance = ShoppingCart()
        return ShoppingCart._instance

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product):
        self.items.remove(product)

    def total_price(self):
        return sum([item.price for item in self.items])

    def list_items(self):
        return [item.get_info() for item in self.items]
