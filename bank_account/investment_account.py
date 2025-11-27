__author__ = "Nick Martens"
__version__ = "1.0.0"
__credits__ = ""

from .bank_account import BankAccount
from datetime import date, timedelta
from patterns.strategy import *

class InvestmentAccount(BankAccount):
    """
    A subclass of the BankAccount class representing an
        investment account of a bank account.
    
    """

    def __init__(self, account_number: int, client_number: int, 
                balance: float, date_created: date, management_fee: float):
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
            management_fee (float): A float value representing the
                bank's management fee.

        Returns:
            None

        Raises:
            ValueError: Raised when the account number or client number
                isn't an integer value.
        
        """
        super().__init__(account_number, client_number, balance, date_created)

        self.__strategy = ManagementFeeStrategy(date_created, management_fee)

        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)
        try:
            self.__management_fee = float(management_fee)
        except:
            self.__management_fee = 2.55

    def __str__(self) -> str:
        """
        Returns a string representation of the investment account 
            instance.

        Returns:
            str: A formatted string representing the investment account
                object.
        
        """
        date_created = self._date_created
        formatted_string = super().__str__()
        if self._date_created <= self.TEN_YEARS_AGO:
            formatted_string += (f"Date Created: {date_created} Management Fee:"
            " Waived Account Type: Investment")
        else:
            formatted_string += (f"Date Created: {date_created} Management Fee:"
            f" ${self.__management_fee:,.2f} Account Type: Investment")
        return formatted_string
    
    def get_service_charges(self) -> float:
        """
        Calculates the service charge and returns the service charge.

        Returns:
            float: The calculated service charge.
        
        """
        service_charge = self.__strategy.calculate_service_charges(self)
        return service_charge
    