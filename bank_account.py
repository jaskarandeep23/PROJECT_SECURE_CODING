from abc import ABC, abstractmethod
from datetime import date


def validate_amount(amount):
    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a number")
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")


class BankAccount(ABC):
    BASE_SERVICE_CHARGE = 0.50

    def __init__(self, account_number, balance, date_created):
        self._account_number = account_number

        try:
            self._balance = float(balance)
        except (TypeError, ValueError):
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
        validate_amount(amount)
        self._balance += float(amount)

    def withdraw(self, amount):
        validate_amount(amount)

        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= float(amount)

    def __str__(self):
        return f"Account Number: {self._account_number} Balance: ${self._balance:.2f}"

    @abstractmethod
    def get_service_charges(self):
        raise NotImplementedError("Subclasses must implement get_service_charges()")