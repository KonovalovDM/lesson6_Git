# lesson6_Git

___inheritance and encapsulation___</br>
***Наследование и инкапсуляция***


Код сформирован для управления учетными записями пользователей для небольшой компании
с использованием объектно-ориентированного программирования на Python.</br>
Компания разделяет сотрудников на обычных работников и администраторов, в коде программы
создаем два класса: `User` и `Admin`, где `Admin` является подклассом `User`.</br>
У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.</br>
Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.