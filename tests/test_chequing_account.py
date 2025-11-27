"""This module defines the TestChequingAccount class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_chequing_account.py
"""

__author__ = "Nick Martens"
__version__ = "1.0.0"
__credits__ = ""

import unittest
from bank_account.chequing_account import ChequingAccount
import datetime

class TestChequingAccount(unittest.TestCase):

    def setUp(self):
        self.__test_date = datetime.date(2024, 5, 15)

    def test_init_attributes_set_to_input_values(self):

        # Act
        output = ChequingAccount(10, 10, 250, self.__test_date, -100, 0.10)

        # Assert
        self.assertEqual(output._date_created, datetime.date(2024, 5, 15))
        self.assertEqual(output._BankAccount__account_number, 10)
        self.assertEqual(output._BankAccount__client_number, 10)
        self.assertEqual(output._BankAccount__balance, 250)
        self.assertEqual(output._ChequingAccount__overdraft_limit, -100)
        self.assertEqual(output._ChequingAccount__overdraft_rate, 0.10)

    def test_init_overdraft_limit_invalid_type(self):

        # Act
        output = ChequingAccount(10, 10, 250, self.__test_date, "INVALID", 
                                0.10)

        # Assert
        self.assertEqual(output._ChequingAccount__overdraft_limit, -100)

    def test_init_overdraft_rate_invalid_type(self):

        # Act
        output = ChequingAccount(10, 10, 250, self.__test_date, -100, 
                                "INVALID")

        # Assert
        self.assertEqual(output._ChequingAccount__overdraft_rate, 0.05)
    
    def test_init_date_created_invalid_type(self):

        # Act
        output = ChequingAccount(10, 10, 250, "INVALID", -100, 0.10)

        # Assert
        self.assertEqual(output._date_created, datetime.date.today())

    def test_get_service_charges_balance_greater_than_overdraft_limit(self):

        # Act
        output = ChequingAccount(10, 10, 250, self.__test_date, -100, 
                                0.10).get_service_charges()
        
        # Assert
        self.assertEqual(output, 0.5)

    def test_get_service_charges_balance_less_than_overdraft_limit(self):

        # Act
        output = ChequingAccount(10, 10, -200, self.__test_date, -100, 
                                0.10).get_service_charges()
        
        # Assert
        self.assertEqual(output, 10.5)

    def test_get_service_charges_balance_equal_to_overdraft_limit(self):

        # Act
        output = ChequingAccount(10, 10, -100, self.__test_date, -100, 
                                0.10).get_service_charges()
        
        # Assert
        self.assertEqual(output, 0.5)

    def test_str_returns_correct_formatted_string(self):

        # Arrange
        expected = ("Account Number: 10 Balance: $-100.00\n"
                            "Overdraft Limit: $-100.00 Overdraft Rate: 10.00%"
                            " Account Type: Chequing\n")

        # Act
        output = ChequingAccount(10, 10, -100, self.__test_date, -100, 
                                0.10).__str__()
        
        # Assert
        self.assertEqual(output, expected)
