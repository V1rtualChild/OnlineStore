from cart import ShoppingCart

class Order:
    def __init__(self, customer_name, delivery_method):
        self.customer_name = customer_name
        self.delivery_method = delivery_method
        self.products = []
        self.total = 0
        self.status = "Створено"
        self.observers = []
        self.delivery_strategy = None

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for obs in self.observers:
            obs.update(self)

    def build_order(self):
        cart = ShoppingCart.get_instance()
        self.products = cart.items.copy()
        self.total = cart.total_price()
        self.status = "Готовий до обробки"
        self.notify()

    def change_status(self, new_status):
        self.status = new_status
        self.notify()

    def set_delivery_strategy(self, strategy):
        self.delivery_strategy = strategy

    def deliver_order(self):
        if self.delivery_strategy:
            self.delivery_strategy.deliver(self)
        else:
            print("⚠️ Спосіб доставки не встановлений.")