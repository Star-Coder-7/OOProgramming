import datetime
import pytz
import random


class Account:
    """Simple account class with __balance (money)."""

    @staticmethod   # A method where self is not needed
    def _currentTime():
        utcTime = datetime.datetime.utcnow()
        return pytz.utc.localize(utcTime)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transactionList = [(Account._currentTime(), balance)]
        print(f"The account created for: " + self._name)
        self.showBalance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.showBalance()
            self._transactionList.append((Account._currentTime(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transactionList.append((Account._currentTime(), -amount))
        else:
            print("You can only withdraw an amount more than 0 and an amount less than or equal to your __balance.")
        self.showBalance()

    def showBalance(self):
        print(f"Your __balance is {self.__balance}")

    def showTransactions(self):
        for date, amount in self._transactionList:
            if amount > 0:
                tranType = "deposited"
            else:
                tranType = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tranType, date, date.astimezone()))


if __name__ == '__main__':
    shiven = Account("Shiven", 0)
    shiven.showBalance()

    shiven.deposit(1000)
    # shiven.showBalance()
    shiven.withdraw(500)
    # shiven.showBalance()

    shiven.withdraw(2000)

    shiven.showTransactions()

    bill = Account("Bill", 800)
    bill.__balance = 200
    bill.deposit(100)
    bill.withdraw(200)
    bill.showTransactions()
    bill.showBalance()
    print(bill.__dict__)

