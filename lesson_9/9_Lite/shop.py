from classes.products import Electronics, Clothing, Household_chemicals
from classes.users import Customer, Admin
from classes.shoping_carts import ShoppingCart


# Создаем продукты
laptop = Electronics(name="Ноутбук", price=120000, brand="Dell", warranty_period=2)
tshirt = Clothing(name="Футболка", price=200, size="M", material="Хлопок")
chemicals = Household_chemicals(name="Средство для мытья посуды", price=120, brand="Fairy", category="Для кухни")

# Создаем пользователей
customer = Customer(username="Иван", email="python@derkunov.ru", address="033 Russ Bur")
admin = Admin(username="Администратор", email="root@derkunov.ru", admin_level=5)

# Создаем корзину покупок для пользователя Иван
cart = ShoppingCart(customer)
cart.add_item(laptop, 1)
cart.add_item(tshirt, 3)
cart.add_item(chemicals, 2)

# Выводим детали корзины до регистрации администратором
print(cart.get_details(), "\n")

# Регистрация корзины администратором
cart.registration(admin)

# Выводим детали корзины после регистрации администратором
print(cart.get_details())
