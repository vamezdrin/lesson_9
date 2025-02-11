class Customer:
    # Контсруктор с двумя атрибутами
    def __init__(self, name: str, orders=[]):
        self.name = name
        self.orders = orders

    # Метод для вывода содержимого на экран
    def __str__(self):
        return f"Клиент (Имя={self.name}, {self.orders})"
    
    # Метод для вывода содержимого на экран
    def __repr__(self):
        return f"Клиент (Имя={self.name}, {self.orders})"