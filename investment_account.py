
from datetime import date, timedelta
from .bank_account import BankAccount

class InvestmentAccount(BankAccount):
    TEN_YEARS_AGO = date.today() - timedelta(days=int(10 * 365.25))

    def __init__(self, account_number, balance, date_created, management_fee=2.55):
        super().__init__(account_number, balance, date_created)

       
        try:
            self.__management_fee = float(management_fee)
        except Exception:
            self.__management_fee = 2.55

    @property
    def management_fee(self):
        return self.__management_fee

    def get_service_charges(self):
        
        if self._date_created <= self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + self.__management_fee

    def __str__(self):
        if self._date_created <= self.TEN_YEARS_AGO:
            fee_display = "Waived"
        else:
            fee_display = f"${self.__management_fee:.2f}"

        return (f"{super().__str__()}\n"
                f"Date Created: {self._date_created} Management Fee: {fee_display} Account Type: Investment")
