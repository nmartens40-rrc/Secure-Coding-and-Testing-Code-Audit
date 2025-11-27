__author__ = "Nick Martens"
__version__ = "1.0.0"
__credits__ = ""

from .service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta
from bank_account.bank_account import BankAccount

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Defines the management fee strategy class and its methods.
    """

    def __init__(self, date_created: date, management_fee: float):
        """
        Args:
            date_created (date): The date the bank account instance 
                was created.
            management_fee (float): A float value representing the
                banks management fee.

        """
        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

        self.__date_created = date_created
        self.__management_fee = management_fee

    def calculate_service_charges(self, account: BankAccount):
        """
        Calculates the service charge and returns the service charge.

        Args:
            account (BankAccount): The current BankAccount instance.

        Returns:
            float: The calculated service charge.
        
        """
        BASE_SERVICE_CHARGE = self.BASE_SERVICE_CHARGE
        if self.__date_created <= self.TEN_YEARS_AGO:
            service_charge = BASE_SERVICE_CHARGE
        else:
            service_charge = BASE_SERVICE_CHARGE + self.__management_fee
        return service_charge
    