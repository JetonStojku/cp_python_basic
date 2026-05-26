""" U 1 """
from datetime import datetime

"""
Ndërtoni një klasë e cila menaxhon account të një klienti të
një banke. Klasa do ketë informacionet: Emër, mbiemër,
balanca, historik trasanksionesh.
"""


class TransactionHistory:
    def __init__(self, amount):
        self.amount = amount
        self.date = datetime.now()

    def __str__(self):
        return f'{self.date}: {self.amount}'


class BankAccount:
    def __init__(self, name: str, surname: str):
        self.name: str = name
        self.surname: str = surname
        self.__balance: float = 0
        self.__history: [TransactionHistory] = []

    def __str__(self):
        return f'{self.name}, {self.surname}'

    def balance(self):
        return self.__balance

    def history(self):
        for transaction in self.__history:
            print(transaction)

    def deposit(self, amount: float):
        if amount <= 0:
            print('Amount should be greater than 0')
        else:
            self.__balance += amount
            self.__history.append(TransactionHistory(amount))

    def withdraw(self, amount: float):
        if amount <= 0:
            print('Amount should be greater than 0')
        elif amount > self.__balance:
            print('Balance should be greater than amount')
        else:
            self.__balance -= amount
            self.__history.append(TransactionHistory(-amount))


client = BankAccount('Alex', 'Hoxa')
print(client, client.balance())
client.deposit(1_000_000)
print(client, client.balance())
client.withdraw(200_000)
print(client, client.balance())
client.deposit(-1_000)
print(client, client.balance())
client.withdraw(-1_000)
print(client, client.balance())
client.withdraw(1_000_000)
print(client, client.balance())
client.withdraw(80_000)
client.withdraw(20_000)
client.withdraw(10_000)
client.deposit(1_000)
client.history()
