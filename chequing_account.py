from .bank_account import BankAccount

class ChequingAccount(BankAccount):
    def __init__(self, account_number, balance, date_created, overdraft_limit=-100.0, overdraft_rate=0.05):
        super().__init__(account_number, balance, date_created)

        
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except Exception:
            self.__overdraft_limit = -100.0

        
        try:
            self.__overdraft_rate = float(overdraft_rate)
        except Exception:
            self.__overdraft_rate = 0.05

    @property
    def overdraft_limit(self):
        return self._overdraft_limit

    @property
    def overdraft_rate(self):
        return self._overdraft_rate

    def get_service_charges(self):
        if self._balance >= self.__overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + (self.__overdraft_limit - self._balance) * self.__overdraft_rate

    def __str__(self):
        return (f"{super().__str__()}\n"
                f"Overdraft Limit: ${self.__overdraft_limit:.2f} "
                f"Overdraft Rate: {self.__overdraft_rate*100:.2f}% Account Type: Chequing")
