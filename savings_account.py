
from .bank_account import BankAccount

class SavingsAccount(BankAccount):
    SERVICE_CHARGE_PREMIUM = 2.0  

    def __init__(self, account_number, balance, date_created, minimum_balance=50.0):
        super().__init__(account_number, balance, date_created)

        
        try:
            self.__minimum_balance = float(minimum_balance)
        except Exception:
            self.__minimum_balance = 50.0

    @property
    def minimum_balance(self):
        return self.__minimum_balance

    def get_service_charges(self):
        if self._balance >= self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM

    def __str__(self):
        return (f"{super().__str__()}\n"
                f"Minimum Balance: ${self.__minimum_balance:.2f} Account Type: Savings")
