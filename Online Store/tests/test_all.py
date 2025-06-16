import pytest
from products.factory import ProductFactory, Book, Laptop, TShirt
from cart import ShoppingCart
from order import Order
from notifier import EmailNotifier, SMSNotifier, LoggerNotifier
from strategy import CourierDelivery, NovaPoshtaDelivery, PickupDelivery

# === 1-5: Factory Pattern ===

def test_create_book():
    p = ProductFactory.create_product("book", "Book A", 100)
    assert isinstance(p, Book)

def test_create_laptop():
    p = ProductFactory.create_product("laptop", "Laptop A", 1000)
    assert isinstance(p, Laptop)

def test_create_tshirt():
    p = ProductFactory.create_product("tshirt", "Tee A", 300)
    assert isinstance(p, TShirt)

def test_invalid_type_raises():
    with pytest.raises(ValueError):
        ProductFactory.create_product("food", "Invalid", 100)

def test_product_info_contains_name_and_price():
    p = ProductFactory.create_product("book", "Test Book", 250)
    assert "Test Book" in p.get_info()
    assert "250" in p.get_info()

# === 6-9: Singleton (Cart) ===

def test_singleton_cart():
    cart1 = ShoppingCart.get_instance()
    cart2 = ShoppingCart.get_instance()
    assert cart1 is cart2

def test_cart_add_and_total():
    cart = ShoppingCart.get_instance()
    cart.items.clear()
    cart.add_product(ProductFactory.create_product("book", "A", 100))
    cart.add_product(ProductFactory.create_product("book", "B", 200))
    assert cart.total_price() == 300

def test_cart_clear_and_total_zero():
    cart = ShoppingCart.get_instance()
    cart.items.clear()
    assert cart.total_price() == 0

def test_cart_add_multiple_items():
    cart = ShoppingCart.get_instance()
    cart.items.clear()
    for _ in range(3):
        cart.add_product(ProductFactory.create_product("tshirt", "Shirt", 100))
    assert len(cart.items) == 3

# === 10-13: Builder (Order) ===

def test_order_build_sets_products_and_total():
    cart = ShoppingCart.get_instance()
    cart.items.clear()
    cart.add_product(ProductFactory.create_product("book", "Python", 400))
    order = Order("Юля", "Courier")
    order.build_order()
    assert len(order.products) == 1
    assert order.total == 400
    assert order.status == "Готовий до обробки"

def test_order_change_status():
    order = Order("Юля", "Nova Poshta")
    order.change_status("Доставляється")
    assert order.status == "Доставляється"

def test_order_with_empty_cart():
    cart = ShoppingCart.get_instance()
    cart.items.clear()
    order = Order("Остап", "Pickup")
    order.build_order()
    assert order.total == 0

def test_order_products_list_copy():
    cart = ShoppingCart.get_instance()
    cart.items.clear()
    prod = ProductFactory.create_product("book", "Separate", 150)
    cart.add_product(prod)
    order = Order("Test", "Courier")
    order.build_order()
    assert prod in order.products

# === 14-16: Observer ===

def test_notify_email(capsys):
    order = Order("Client", "Courier")
    order.attach(EmailNotifier())
    order.change_status("Виконано")
    output = capsys.readouterr().out
    assert "[Email]" in output


def test_notify_sms_and_logger(capsys):
    order = Order("Client", "Nova Poshta")
    order.attach(SMSNotifier())
    order.attach(LoggerNotifier())
    order.change_status("Скасовано")
    output = capsys.readouterr().out
    assert "[SMS]" in output
    assert "[Log]" in output

def test_no_observers():
    order = Order("NoObs", "Pickup")
    try:
        order.change_status("Очікує")
    except Exception:
        pytest.fail("Observer notification raised exception unexpectedly!")

# === 17-20: Strategy ===

def test_strategy_courier(capsys):
    order = Order("Test", "Courier")
    order.set_delivery_strategy(CourierDelivery())
    order.deliver_order()
    out = capsys.readouterr().out
    assert "Кур'єр доставить" in out

def test_strategy_nova_poshta(capsys):
    order = Order("Test", "Nova")
    order.set_delivery_strategy(NovaPoshtaDelivery())
    order.deliver_order()
    out = capsys.readouterr().out
    assert "Нову Пошту" in out  # було: Нова Пошта

def test_strategy_pickup(capsys):
    order = Order("Test", "Pickup")
    order.set_delivery_strategy(PickupDelivery())
    order.deliver_order()
    out = capsys.readouterr().out
    assert "забрати" in out

def test_strategy_not_set(capsys):
    order = Order("Test", "None")
    order.deliver_order()
    out = capsys.readouterr().out
    assert "не встановлений" in out
