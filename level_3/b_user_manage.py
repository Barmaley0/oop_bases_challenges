"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self):
        self.usernames = []

    def add_user(self, username):
        self.usernames.append(username)

    def get_users(self):
        return self.usernames


class AdminManager(UserManager):
    def __init__(self):
        super().__init__()

    def ban_username(self, username):
        if username in self.usernames:
            self.usernames.remove(username)
        else:
            print("Такого пользователя не существует.")


class SuperAdminManager(AdminManager):
    def __init__(self):
        super().__init__()

    def ban_all_users(self):
        self.usernames.clear()


if __name__ == "__main__":
    user_manager = UserManager()
    list_of_users = ["Bob", "John", "Tom", "Sam", "Kate"]
    for username in list_of_users:
        user_manager.add_user(username)

    print(f"All users: {user_manager.get_users()}")

    admin_manager = AdminManager()
    admin_manager.usernames = user_manager.get_users()
    ban_list = ["Bob", "John", "Tony"]
    for username in ban_list:
       admin_manager.ban_username(username)

    print(f"All users: {user_manager.get_users()}")

    super_admin_manager = SuperAdminManager()
    super_admin_manager.usernames = user_manager.get_users()
    super_admin_manager.ban_all_users()

    print(f"All users: {user_manager.get_users()} list empty.")
