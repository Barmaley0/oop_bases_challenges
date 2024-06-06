"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        if income <= 0:
            raise ValueError("Income must be a positive number.")
        self.balance += income

    def decrease_balance(self, expense: float):
        if expense <= 0:
            raise ValueError("expense must be a positive number.")
        if self.balance - expense < 0:
            raise ValueError("The balance cannot be negative.")
        self.balance -= expense

if __name__ == '__main__':
    account = BankAccount("Lev Nikolaevich", 100.01)
    account.decrease_balance(50.32)
    print(f"Balance after decreasing by 50.32: {account.balance:.2f}")
    account.decrease_balance(100.50)
    print(f"Balance after decreasing by 100.50: {account.balance:.2f}")
    account.increase_balance(50.50)
    print(f"Balance after increase by 55.50: {account.balance:.2f}")
    if account.balance < 0:
        raise ValueError("The balance cannot be negative.")
