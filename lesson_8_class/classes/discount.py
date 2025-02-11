class Discount:
    # Контсруктор с двумя атрибутами
    def __init__(self, description: str, discount_percent: float):
        self.description = description
        self.discount_percent = discount_percent

    # Метод для вывода содержимого на экран
    def __str__(self):
        return f"Продукт (Описание скидки={self.description}, Процент={self.discount_percent})"
    
    # Метод для вывода содержимого на экран
    def __repr__(self):
        return f"Продукт (Описание скидки={self.description}, Процент={self.discount_percent})"
    
    # Статический метод для рассчета цены со скидкой
    @staticmethod
    def calculate_discounted_price(price, discount_percent):
        return price * (1 - discount_percent / 100)
    
    # Статический метод для применения различных видов скидок 
    @staticmethod
    def type_disconted_price(type_disconted):
        if type_disconted == 'Сезонная скидка':
            return 5
        elif type_disconted == 'Скидка по промокоду':
            return 10
        elif type_disconted == 'Скидка для пенсионеров':
            return 25
        return None