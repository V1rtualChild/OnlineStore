from products.factory import ProductFactory
from cart import ShoppingCart
from order import Order
from notifier import EmailNotifier, SMSNotifier, LoggerNotifier
from strategy import CourierDelivery, NovaPoshtaDelivery, PickupDelivery

book = ProductFactory.create_product("book", "YOU", 250)
laptop = ProductFactory.create_product("laptop", "MacBook Pro M1", 40000)
tshirt = ProductFactory.create_product("tshirt", "Sainty", 499)
order = Order(customer_name="Остап", delivery_method="Кур'єр")


cart = ShoppingCart.get_instance()
cart.add_product(book)
cart.add_product(laptop)
cart.add_product(tshirt)

order.attach(EmailNotifier())
order.attach(SMSNotifier())
order.attach(LoggerNotifier())

order.build_order()

order.set_delivery_strategy(CourierDelivery())
order.deliver_order()

order.set_delivery_strategy(NovaPoshtaDelivery())
order.deliver_order()

order.set_delivery_strategy(PickupDelivery())
order.deliver_order()

print("🛒 Вміст кошика:")
for info in cart.list_items():
    print("-", info)

print(f"💰 Загальна сума: {cart.total_price()} грн")

order.change_status("Відправлено")
order.change_status("Доставлено")
