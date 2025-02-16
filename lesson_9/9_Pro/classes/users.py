import hashlib

# Базовый класс, представляющий пользователя
class User:
    users = []  # Список для хранения всех пользователей
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.hash_password(password).hexdigest()
        User.users.append(self)

    def get_details(self):
        return f"Пользователь: {self.username}, Email: {self.email}, Хешированный пароль: {self.password}"
        
    # Хеширование пароля
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode())

    # Проверка пароля
    @staticmethod
    def check_password(stored_password, provided_password):
        if provided_password == stored_password:
            return True
        else: 
            return False

# Класс, представляющий клиента, наследующий класс User.
class Customer(User):
    def __init__(self, username, email, password, address):
        super().__init__(username, email, password)
        self.address = address

    def get_details(self):
        return f"Клиент: {self.username}, Email: {self.email}, Адрес: {self.address}, Хешированный пароль: {self.password}"

# Класс, представляющий администратора, наследующий класс User.
class Admin(User):
    def __init__(self, username, email, password, admin_level):
        super().__init__(username, email, password)
        self.admin_level = admin_level

    def get_details(self):
        return f"Admin: {self.username}, Email: {self.email}, Admin-Level: {self.admin_level}, Хешированный пароль: {self.password}"
    
    # Выводит список всех пользователей.
    @staticmethod
    def list_users():
        list_user = []
        for users in User.users:
            list_user.append(users.get_details())
        return f"Список пользователей:\n{list_user}"
    
    # Удаляет пользователя по имени пользователя.
    @staticmethod
    def delete_user(username):
        for user in User.users:
            if user.get_details().find(username) != -1:
                User.users.remove(user)
                return f'Пользователь {username} удален из системы'
            else:
                return f'Пользователя {username} нет в системе'
            