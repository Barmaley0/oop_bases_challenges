"""
Нам неоюходимо проверить, находится ли фамилия пользователя в списке запрещенных.

Задания:
    1. Cоздайте класс юзера, у которого параметры: имя, фамилия, возраст.
    2. Добавьте ему метод should_be_banned, который проверяет, должен ли быть пользователь забанен.
       Пользователя стоит забанить, если его фамилия находится в SURNAMES_TO_BAN.
"""

SURNAMES_TO_BAN = ['Vaughn', 'Wilhelm', 'Santaros', 'Porter', 'Smith']


class User:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def should_be_banned(self):
        return self.surname in SURNAMES_TO_BAN

    def get_info(self):
        return f"User {self.name} is {'' if self.should_be_banned() else 'not'} banned"
