# Базовый класс, представляющий пользователя.
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_details(self):
        return f"Пользователь: {self.username}, Email: {self.email}"
    
    # Метод возвращающий имя пользователя
    def get_name(self):
        return self.username

# Класс, представляющий клиента, наследующий класс User.
class Customer(User):
    def __init__(self, username, email, address):
        super().__init__(username, email)
        self.address = address

    def get_details(self):
        return f"Клиент: {self.username}, Email: {self.email}, Адрес: {self.address}"
    
    def is_admin(self):
        return False

# Класс, представляющий администратора, наследующий класс User.
class Admin(User):
    def __init__(self, username, email, admin_level):
        super().__init__(username, email)
        self.admin_level = admin_level
    
    def is_admin(self):
        return True

    def get_details(self):
        return f"Admin: {self.username}, Email: {self.email}, Admin-Level: {self.admin_level}"
