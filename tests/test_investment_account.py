"""This module defines the TestInvestmentAccount class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_investment_account.py
"""

__author__ = "Nick Martens"
__version__ = "1.0.0"
__credits__ = ""

from bank_account.investment_account import InvestmentAccount
from datetime import *
import unittest

class TestInvestmentAccount(unittest.TestCase):

    def setUp(self):
        self.__test_date = date(2024, 5, 15)
        self.__TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)
        self.__MORE_THAN_TEN_YEARS_AGO = date(2010, 5, 15)

    def test_init_attributes_set_to_input_values(self):

        # Act
        output = InvestmentAccount(20, 20, 100, self.__test_date, 2)

        # Assert
        self.assertEqual(output._date_created, date(2024, 5, 15))
        self.assertEqual(output._BankAccount__account_number, 20)
        self.assertEqual(output._BankAccount__client_number, 20)
        self.assertEqual(output._BankAccount__balance, 100)
        self.assertEqual(output._InvestmentAccount__management_fee, 2)

    def test_init_management_fee_is_invalid_type(self):

        # Act
        output = InvestmentAccount(20, 20, 100, self.__test_date, "INVALID")

        # Assert
        self.assertEqual(output._InvestmentAccount__management_fee, 2.55)

    def test_get_service_charges_date_created_more_than_ten_years_ago(self):

        # Act
        output = InvestmentAccount(20, 20, 100, 
                                   self.__MORE_THAN_TEN_YEARS_AGO, 2)

        # Assert
        self.assertEqual(output.get_service_charges(), 0.5)

    def test_get_service_charges_date_created_exactly_ten_years_ago(self):

        # Act
        output = InvestmentAccount(20, 20, 100, self.__TEN_YEARS_AGO, 2)

        # Assert
        self.assertEqual(output.get_service_charges(), 0.5)

    def test_get_service_charges_date_created_newer_than_ten_years_ago(self):

        # Act
        output = InvestmentAccount(20, 20, 100, self.__test_date, 2)

        # Assert 
        self.assertEqual(output.get_service_charges(), 2.5)

    def test_str_displays_waived_management_fee(self):

        # Arrange
        expected = (f"Account Number: 20 Balance: $100.00\n"
                    f"Date Created: {self.__TEN_YEARS_AGO} Management Fee: "
                    "Waived"
                    " Account Type: Investment")
        
        # Act
        output = InvestmentAccount(20, 20, 100, self.__TEN_YEARS_AGO, 2)

        # Assert
        self.assertEqual(output.__str__(), expected)

    def test_str_displays_management_fee_when_account_is_not_ten_years_old\
        (self):
        
        # Arrange
        expected = (f"Account Number: 20 Balance: $100.00\n"
                    f"Date Created: {self.__test_date} Management Fee: $2.00"
                    " Account Type: Investment")
        
        # Act
        output = InvestmentAccount(20, 20, 100, self.__test_date, 2)

        # Assert
        self.assertEqual(output.__str__(), expected)
