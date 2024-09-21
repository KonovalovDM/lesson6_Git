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
        print(f'{self._name} выполняет свою работу')






    # Описываем методы присущие родительскому классу
    def public_id(self):
        return f'Это открытый метод. Пользователь: {name} с идентификатором: {id}'

    def __private_access_level(self):
        return f'Это приватный метод. Админ по имени {name} с идентификатором: {id} и уровнем доступа {access_level}'

    def access_level(self):
        self.__private_access_level = user

    def user_work(self):
        print(f'Ввод данных в систему, редактирование и удаление данных')



# Создаем дочерний класс администраторов
class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, ac  )
        self.__privet_access_level = access_level

    # Описываем специфические методы присущие только дочернему классу
    def add_user(self):
        print(f'Добавление пользователя: {name} с идентификатором: {id}')

    def remove_user(self):
        print(f'Удаление пользователя: {name} с идентификатором: {id}')

    def get_details(self):
        details = (f'{self.public_id} - идентификатор пользователя с именем {self.public_name} '
                   f'и уровнем доступа{self.__privet_access_level}')
        return details

    def set_private(self, value):
        self.__privet_access_level = (value)
        return value



# Создаем экземпляры класса 'Admin'
admin1 = Admin(1, "Ермаков Юрий", 1)
admin2 = Admin(2, "Сизенкова Ольга", 1)

# Добавляем экземпляр класса 'User'
user1.add_user(3, "Васильев Иван")
user2.add_user(4, "Иванов Василий")
user3.add_user(5, "Маринина Мария")
user4.add_user(6, "Кузнецова Ольга")

user2.user_work('Очень интересная информация')

user3.remove_user(5, "Маринина Мария")
