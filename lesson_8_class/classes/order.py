class Order:
    _total_orders = 0
    _total_price = 0
    
    # Контсруктор c атрибутом: products
    def __init__(self, products):
        self.products = products
        Order._total_price += self.total_price()
        Order._total_orders += 1

    # Метод класса для вывода общего количества заказов
    @classmethod
    def total_orders(cls):
        return cls._total_orders
    
    # Метод для вычисления общей стоимости всех товаров для клиента
    def total_price(self):
        return sum(product.price for product in self.products)
    
    # Метод класса для вычисления общей стоимости всех товаров
    @classmethod
    def total_all_price(cls):
       return cls._total_price

    # Метод для вывода содержимого на экран
    def __str__(self):
        total_order = 'Заказ ('
        for product in self.products:
            total_order += f"{product.name}-{product.price} руб.,"
        total_order += ')'
        return total_order
    
    # Метод для вывода содержимого на экран
    def __repr__(self):
        total_order = 'Заказ ('
        for product in self.products:
            total_order += f"{product.name}-{product.price} руб.,"
        total_order += ')'
        return total_order