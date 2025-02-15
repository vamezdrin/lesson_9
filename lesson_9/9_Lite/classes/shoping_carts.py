# Класс, представляющий корзину покупок.
class ShoppingCart:
    def __init__(self, user):
        self.items = []
        self.user = user
        self.reg_admin = "Не зарегестрирован"
    
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
    
    # Регистрация товара администратором
    def registration(self, admin):
        if admin.is_admin() == True:
            self.reg_admin = admin.get_name()
        else:
            print("Пользователь не может зарегестрировать товар!\n")
        
    # Возвращает детализированную информацию о содержимом корзины и общей стоимости
    def get_details(self):
        if self.user.is_admin() == False:
            details = f"Покупатель {self.user.get_name()} приобрел\nКорзина покупок:\n"
            for item in self.items:
                details += f"{item['Продукт'].get_details()}, Количество: {item['количество']}\n"
            details += f"Общее: {self.get_total()} руб\nЗарегестрировал товар пользователь {self.reg_admin}"
            return details
        else:
            return f"Администратор {self.user.get_name()} на может покупать товар"