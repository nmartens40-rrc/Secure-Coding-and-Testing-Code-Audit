__author__ = "Nick Martens"
__version__ = "1.0.0"
__credits__ = ""

from .service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Defines the minimum balance strategy class and its methods.
    """

    def __init__(self, minimum_balance: float):
        """
        Args:
            minimum_balance (float): The minimum balance the account
                instance.
        
        """
        self.__minimum_balance = minimum_balance
        self.SERVICE_CHARGE_PREMIUM = 2.0

    def calculate_service_charges(self, account: BankAccount):
        """
        Calculates the service charge and returns the service charge.

        Args:
            account (BankAccount): The current BankAccount instance.

        Returns:
            float: The calculated service charge.
        
        """
        balance = account.balance

        if balance >= self.__minimum_balance:
            service_charge = self.BASE_SERVICE_CHARGE
        else:
            service_charge = self.BASE_SERVICE_CHARGE * \
            self.SERVICE_CHARGE_PREMIUM
        return service_charge
