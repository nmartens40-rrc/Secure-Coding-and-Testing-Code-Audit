__author__ = "Nick Martens"
__version__ = "1.0.0"
__credits__ = ""

from .service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Defines the overdraft strategy class and its methods.
    """

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Args:
            overdraft_limit (float): The overdraft limit of an account
                instance.
            overdraft_rate (float): The overdraft rate of an account
                instance.

        Returns:
            None

        Raises:
            ValueError: Raised when the account number or client number
                isn't an integer value.
                
        """
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculates the service charge and returns the service charge.

        Returns:
            float: The calculated service charge.
        
        """
        balance = account.balance
        BASE_SERVICE_CHARGE = self.BASE_SERVICE_CHARGE

        if balance >= self.__overdraft_limit:
            service_charge = BASE_SERVICE_CHARGE
        else:
            service_charge = (BASE_SERVICE_CHARGE + \
                (self.__overdraft_limit - balance) * 
                    self.__overdraft_rate)
        return service_charge
