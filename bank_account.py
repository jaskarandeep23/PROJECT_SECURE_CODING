
from abc import ABC, abstractmethod
from datetime import date

class BankAccount(ABC):
    BASE_SERVICE_CHARGE = 0.50

    def __init__(self, account_number, balance, date_created):
        self._account_number = account_number
        
        
        try:
            self._balance = float(balance)
        except Exception:
            self._balance = 0.0

       
        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()

    @property
    def balance(self):
        return self._balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def date_created(self):
        return self._date_created

    def deposit(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit amount must be positive numeric value.")

    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self._balance -= amount
        else:
            raise ValueError("Withdrawal amount must be positive numeric value.")

    def __str__(self):
        return f"Account Number: {self._account_number} Balance: ${self._balance:.2f}"

    @abstractmethod
    def get_service_charges(self):
        raise NotImplementedError
