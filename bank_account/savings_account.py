__author__ = "Nick Martens"
__version__ = "1.0.0"
__credits__ = ""

from .bank_account import BankAccount
from datetime import date
from patterns.strategy import *

class SavingsAccount(BankAccount):
    """
    A subclass of the BankAccount class representing a
        savings account of a bank account.
    
    """
    
    def __init__(self, account_number: int, client_number: int, 
                balance: float, date_created: date, minimum_balance: float):
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
            minimum_balance (float): A float value representing the
                minimum balance of a savings account.

        Returns:
            None

        Raises:
            ValueError: Raised when the account number or client number
                isn't an integer value.
        
        """
        super().__init__(account_number, client_number, balance, date_created)

        self.__strategy = MinimumBalanceStrategy(minimum_balance)

        self.__balance = self.balance

        try:
            self.__minimum_balance = float(minimum_balance)
        except:
            self.__minimum_balance = 50

    def __str__(self) -> str:
        """
        Returns a string representation of the savings account 
            instance.

        Returns:
            str: A formatted string representing the savings account
                object.
        
        """
        formatted_string = super().__str__()
        formatted_string += (f"Minimum Balance: ${self.__minimum_balance:,.2f}"
                            " Account Type: Savings")
        return formatted_string
    
    def get_service_charges(self) -> float:
        """
        Calculates the service charge and returns the service charge.

        Returns:
            float: The calculated service charge.
        
        """
        service_charge = self.__strategy.calculate_service_charges(self)
        return service_charge
    