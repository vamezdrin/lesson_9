class Product:
    # Контсруктор с двумя атрибутами: name (название товара) и price (цена товара)
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        
    # Дандер метод для сравнения товаров по цене ==
    def __eq__(self, other):
        return self.price == other.price
    
    # Дандер метод для сравнения товаров по цене <
    def __lt__(self, other):
        return self.price < other.price
    
    # Метод для вывода содержимого на экран
    def __str__(self):
        return f"Продукт (Название={self.name}, Цена={self.price})"
    
    # Метод для вывода содержимого на экран
    def __repr__(self):
        return f"Продукт (Название={self.name}, Цена={self.price})"