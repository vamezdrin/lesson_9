from classes.order import Order
from classes.product import Product
from classes.сustomer import Customer
from classes.discount import Discount

# Создаем продукты
product1 = Product("Молоко", 50)
product2 = Product("Хлеб", 75)
product3 = Product("Масло", 100)

# Рассчитываем цену с учетом скидки
product1.price = Discount.calculate_discounted_price(product1.price, Discount.type_disconted_price('Сезонная скидка'))
product2.price = Discount.calculate_discounted_price(product2.price, Discount.type_disconted_price('Скидка по промокоду'))
product3.price = Discount.calculate_discounted_price(product3.price, Discount.type_disconted_price('Скидка для пенсионеров'))

# Вывод продуктов с примененной скидкой
print(product1)
print(product2)
print(product3, '\n')

# Создаем клиентов
client1 = Customer("Иван")
client2 = Customer("Олег")
client3 = Customer("Юрий")

# Создаем заказы
order1 = Order([product1])
order2 = Order([product1, product3])
order3 = Order([product1, product2, product3])

# Выводим на экран заказы
print(repr(order1))
print(repr(order2))
print(repr(order3), '\n')

# Добавляем заказы клиентам
client1.orders = order1
client2.orders = order2
client3.orders = order3

# Выводим на экран клиентов с заказами
print(client1)
print(client2)
print(client3, '\n')

# Общее количество заказов
print(f'Общее количество заказов {Order.total_orders()}')
print(f'Общее сумма всех заказов, всех пользователей {Order.total_all_price()}')