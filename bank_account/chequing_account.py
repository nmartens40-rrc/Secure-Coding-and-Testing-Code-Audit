__author__ = "Nick Martens"
__version__ = "1.0.0"
__credits__ = ""

from .bank_account import BankAccount
from datetime import date
from patterns.strategy import *

class ChequingAccount(BankAccount):
    """
    A subclass of the BankAccount class representing a 
        chequing account of a bank account.

    """

    def __init__(self, account_number: int, client_number: int, balance: float,
                date_created: date, overdraft_limit: float, 
                overdraft_rate: float):
        """
        Args:
            account_number (int): An integer value representing the
                bank account number.
            client_number (int): An integer value representing the
                client number representing the account holder.
            balance (float): A float value representing the current
                balance of the bank account.
            date_created (date): A date value representing the date the
                bank account was created.
            overdraft_limit (float): A float value representing the
                overdraft limit.
            overdraft_rate (float): A float value representing the
                overdraft rate.

            Returns:
                None

            Raises:
                ValueError: Raised when the account number or client number
                    isn't an integer value.
        
        """
        super().__init__(account_number, client_number, balance, date_created)

        self.__strategy = OverdraftStrategy(overdraft_limit, overdraft_rate)

        self.__balance = self.balance

        try:
            self.__overdraft_limit = float(overdraft_limit)
        except:
            self.__overdraft_limit = -100

        try:
            self.__overdraft_rate = float(overdraft_rate)
        except:
            self.__overdraft_rate = 0.05

    def __str__(self) -> str:
        """
        Returns a string representation of the chequing account 
            instance.

        Returns:
            str: A formatted string representing the chequing account 
                object.
        
        """
        formatted_string = super().__str__()
        formatted_string += (f"Overdraft Limit: ${self.__overdraft_limit:,.2f}"
                            f" Overdraft Rate: {self.__overdraft_rate * \
                            100:,.2f}%"
                            " Account Type: Chequing\n")
        return formatted_string
        
    def get_service_charges(self) -> float:
        """
        Calculates the service charge and returns the service charge.

        Returns:
            float: The calculated service charge.
        
        """
        service_charge = self.__strategy.calculate_service_charges(self)
        return service_charge
    