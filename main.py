# Система управления учетными записями пользователей

# Создаем родительский класс
class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id             # Защищенный атрибут
        self._name = name                   # Защищенный атрибут
        self._access_level = access_level   # Защищенный атрибут

    # Методы для доступа к защищенным атрибутам
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def work(self):
        print(f'\n{self._name} выполняет свою работу')

# Создаем дочерний класс администраторов
class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self._admin_access_level = 'admin'

        
    # Описываем специфические методы присущие только дочернему классу
    def add_user(self, users_list, user):
        users_list.append(user)
        print(f'Добавлен пользователь: {user.get_name()} c идентификатором - {user.get_user_id()}')

    def remove_user(self, users_list, user):
        users_list.remove(user)
        print(f'\nУдален пользователь:\n {user.get_name()} c идентификатором - {user.get_user_id()}')

    def get_admin_details(self):
        return f'\n{self.get_user_id()} - идентификатор администратора с именем - {self.get_name()} и уровнем доступа - {self.get_access_level()}'

# Создаем список пользователей
users = []

# Создаем экземпляры класса 'Admin'
admin1 = Admin(1, "Ермаков Юрий")
admin2 = Admin(2, "Сизенкова Ольга")

# Добавляем экземпляр класса 'User'
user1 = User(3, "Васильев Иван")
user2 = User(4, "Иванов Василий")
user3 = User(5, "Маринина Мария")
user4 = User(6, "Кузнецова Ольга")

# Используем методы для управления пользователями
admin1.add_user(users, user1)  # Добавление пользователя в список
admin1.add_user(users, user2)  # Добавление пользователя в список
admin1.add_user(users, user3)  # Добавление пользователя в список
admin2.add_user(users, user4)  # Добавление пользователя в список

user2.work()

admin1.remove_user(users, user3)  # Удаление пользователя из списка

# Вывод информации об администраторах
print(admin1.get_admin_details())
print(admin2.get_admin_details())
