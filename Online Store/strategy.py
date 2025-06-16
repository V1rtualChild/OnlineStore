from abc import ABC, abstractmethod

class DeliveryStrategy(ABC):
    @abstractmethod
    def deliver(self, order):
        pass

class CourierDelivery(DeliveryStrategy):
    def deliver(self, order):
        print(f"🚗 Кур'єр доставить замовлення на ім’я {order.customer_name}.")

class NovaPoshtaDelivery(DeliveryStrategy):
    def deliver(self, order):
        print(f"📦 Замовлення для {order.customer_name} буде відправлено через Нову Пошту.")

class PickupDelivery(DeliveryStrategy):
    def deliver(self, order):
        print(f"🏠 {order.customer_name} може забрати замовлення самостійно з пункту видачі.")
