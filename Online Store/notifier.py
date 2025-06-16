class Observer:
    def update(self, order):
        pass

class EmailNotifier(Observer):
    def update(self, order):
        print(f"📧 [Email] Замовлення для {order.customer_name}: статус змінено на '{order.status}'.")

class SMSNotifier(Observer):
    def update(self, order):
        print(f"📱 [SMS] Статус вашого замовлення: {order.status}.")

class LoggerNotifier(Observer):
    def update(self, order):
        print(f"📝 [Log] {order.customer_name}: статус — {order.status}, сума — {order.total} грн.")
