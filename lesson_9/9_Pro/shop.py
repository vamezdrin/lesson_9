from classes.products import Electronics, Clothing
from classes.users import Customer, Admin
from classes.shoping_carts import ShoppingCart
from classes.authentication import AuthenticationService

# Создаем продукты
laptop = Electronics(name="Ноутбук", price=120000, brand="Dell", warranty_period=2)
tshirt = Clothing(name="Футболка", price=200, size="M", material="Хлопок")

# Создаем пользователей
customer = Customer(username="Иван", email="python@derkunov.ru", password="000000", address="ул. Строителей")
admin = Admin(username="Администратор", email="root@derkunov.ru", password="123456", admin_level=5)

# Создаем корзину покупок и добавляем товары
cart = ShoppingCart()
cart.add_item(laptop, 1)
cart.add_item(tshirt, 3)

# Выводим детали корзины
print(cart.get_details())

# Выводим список пользователей под администратором
print(admin.list_users(), '\n')

# Удаляем пользователя Иван под администратором
print(admin.delete_user('Иван'))

authentication = AuthenticationService()

# Создаем нового пользователя
new_user = authentication.register(Customer, "Олег", "admin@mail.ru", "888888", "ул. Ленина")

# Создаем нового пользователя, с именем которое есть в системе
new_user2 = authentication.register(Admin, "Администратор", "ivan@mail.ru", "123456", "ул. Ленина")

# Выводим список пользователей с новым добавленным пользователем
print(admin.list_users(), '\n')

# Авторизуемся
session = authentication.login("Олег", "888888")
print(session)
session2 = authentication.login("Администратор", "124356")
print(session2)

# Запрос текущего авторизованного пользователя
print('Текщией пользователь:\n', authentication.get_current_user(), '\n')

# Разлогинивание текущего пользователя
print(authentication.logout(), '\n')

# Запрос текущего аторизованного пользователь, когда нет ни одгного авторизованного
print('Текщией пользователь:\n', authentication.get_current_user())