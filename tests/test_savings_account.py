"""This module defines the TestSavingsAccount class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_savings_account.py
"""


__author__ = "Nick Martens"
__version__ = "1.0.0"
__credits__ = ""

from bank_account.savings_account import SavingsAccount
from datetime import *
import unittest

class TestSavingsAccount(unittest.TestCase):
    
    def setUp(self):
        self.__test_date = date(2024, 5, 15)

    def test_init_attributes_set_to_input_values(self):

        # Act
        output = SavingsAccount(20, 20, 100, self.__test_date, 20)

        # Assert
        self.assertEqual(output._date_created, date(2024, 5, 15))
        self.assertEqual(output._BankAccount__account_number, 20)
        self.assertEqual(output._BankAccount__client_number, 20)
        self.assertEqual(output._BankAccount__balance, 100)
        self.assertEqual(output._SavingsAccount__minimum_balance, 20)

    def test_init_minimum_balance_is_invalid_type(self):

        # Act
        output = SavingsAccount(20, 20, 100, self.__test_date, "INVALID")

        # Assert
        self.assertEqual(output._SavingsAccount__minimum_balance, 50)

    def test_get_service_charges_balance_greater_than_minimum_balance(self):

        # Act
        output = SavingsAccount(20, 20, 100, self.__test_date, 20)

        # Assert
        self.assertEqual(output.get_service_charges(), 0.5)

    def test_get_service_charges_balance_equal_to_minimum_balance(self):

        # Act
        output = SavingsAccount(20, 20, 100, self.__test_date, 100)

        # Assert
        self.assertEqual(output.get_service_charges(), 0.5)

    def test_get_service_charges_balance_less_than_minimum_balance(self):

        # Act
        output = SavingsAccount(20, 20, 10, self.__test_date, 100)

        # Assert
        self.assertEqual(output.get_service_charges(), 1)

    def test_str_returns_correct_string_format(self):

        # Arrange
        expected = (f"Account Number: 20 Balance: $100.00\n"
                    "Minimum Balance: $20.00 Account Type: Savings")

        # Act
        output = SavingsAccount(20, 20, 100, self.__test_date, 20)

        # Assert
        self.assertEqual(output.__str__(), expected)
        