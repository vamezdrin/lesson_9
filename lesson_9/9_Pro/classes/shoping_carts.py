# Класс, представляющий корзину покупок.
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    # Добавляет продукт в корзину.
    def add_item(self, product, quantity):
        self.items.append({"Продукт": product, "количество": quantity})
    
    # Удаляет продукт из корзины по имени.
    def remove_item(self, product_name):
        self.items = [item for item in self.items if item["Продукт"].name != product_name]
    
    # Возвращает общую стоимость продуктов в корзине.
    def get_total(self):
        total = sum(item["Продукт"].price * item["количество"] for item in self.items)
        return total
    
    # Возвращает детализированную информацию о содержимом корзины и общей стоимости
    def get_details(self):
        details = "Корзина покупок:\n"
        for item in self.items:
            details += f"{item['Продукт'].get_details()}, Количество: {item['количество']}\n"
        details += f"Общее: {self.get_total()} руб"
        return details