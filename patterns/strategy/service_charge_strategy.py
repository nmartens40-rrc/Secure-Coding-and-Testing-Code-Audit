__author__ = "Nick Martens"
__version__ = "1.0.0"
__credits__ = ""

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    Determines which service charge strategy to use.
    """

    BASE_SERVICE_CHARGE = 0.50

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        An abstract method that calls the required calculation method
            depending on the input.

        Returns:
            float: The calculated service charges as a float.
            
        """
        pass