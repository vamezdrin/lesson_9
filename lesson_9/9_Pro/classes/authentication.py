import uuid
from classes.users import User

# Сервис для управления регистрацией и аутентификацией пользователей.
class AuthenticationService:
    def __init__(self):
        self.current_user = ''
        self.current_session = ''
    
    # Регистрация нового пользователя.
    def register(self, user_class, username, email, password, *args):                
        # Проверка имени на уникальность
        flag = 0
        for user in User.users:         
            if user.get_details().find(username) != -1:
                flag = 1  
                                   
        if flag == 0:
            # Регистрация нового пользователя
            print(f'Пользователь {username} зарегестрирован!')
            return user_class(username, email, password, '{}'.format(*args))
        else:
            print(f'Пользователь {username} уже существует в системе. Пожалуйста ввведите другое имя.')

    # Аутентификация пользователя.
    def login(self, username, password):
        session = None
        flag = 0
        # Проверка пользователя и проверка пароля
        for user in User.users:
            if user.get_details().find(username) != -1:
                print(f"Пользователь {username} найден. Проверка пароля ...")
                flag = 1
                hash_pass = str(User.hash_password(password).hexdigest())
                # Проверяем пароль
                '''if user.check_password(, hash_pass):
                    print('Пароль верный')
                else:
                    print('Пароль не верный')'''
                
                # Проверяем пароль
                if user.get_details().find(hash_pass) != -1:
                    self.current_user = username
                    print(f"Пароль верный, пользователь {username} успешно авторизован!")
                    session = uuid.uuid4()
                    
                    # Записываем в память (переменные) какой последний пользователь входил в систему и сессию
                    self.current_user = user.get_details()
                    self.current_session = session 
                else:
                    print(f"Пароль не верный")

                 
        if flag == 0: print(f"Пользователь {username} не найден в системе.")
        return session

    # Выход пользователя из системы.
    def logout(self):
        if self.current_session != '':
            self.current_session = ''
            return f'Пользователь {self.current_user} разавторизован'
        else:
            return 'На данный момент нет авторизованных пользователей'

    
    # Возвращает текущего вошедшего пользователя.
    def get_current_user(self):
        if self.current_session != '' and self.current_user != '':
            return f'Текущий вошедший пользователь: {self.current_user}'
        else:
            return 'На данный момент нет авторизованных пользователей'