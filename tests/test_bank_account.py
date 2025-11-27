"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

__author__ = "Nick Martens"
__version__ = "1.0.1"
__credits__ = ""

import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.bank_account = BankAccount(20, 40, 100)

    
    def test_init_attributes_set_to_valid_input_values(self):

        # Assert
        self.assertEqual(self.bank_account._BankAccount__account_number, 20)
        self.assertEqual(self.bank_account._BankAccount__client_number, 40)
        self.assertEqual(self.bank_account._BankAccount__balance, 100)

    def test_init_balance_set_to_zero_when_input_is_non_numeric(self):

        # Act
        output = BankAccount(20, 40, "INVALID")

        # Assert
        self.assertEqual(output._BankAccount__balance, 0)

    def test_init_valueerror_raised_when_account_number_is_non_numeric(self):

        # Assert
        with self.assertRaises(ValueError):
            BankAccount("INVALID", 40, 100)

    def test_init_valueerror_raised_when_client_number_is_non_numeric(self):

        # Assert
        with self.assertRaises(ValueError):
            BankAccount(20, "INVALID", 100)

    def test_account_number_accessor_valid_object_returns_attribute(self):

        # Assert
        self.assertEqual(self.bank_account.account_number, 20)

    def test_client_number_accessor_valid_object_returns_attribute(self):

        # Assert
        self.assertEqual(self.bank_account.client_number, 40)

    def test_balance_accessor_valid_object_returns_attribute(self):

        # Assert
        self.assertEqual(self.bank_account.balance, 100)

    def test_update_balance_positive_input_updates_balance_correctly(self):

        # Act
        self.bank_account.update_balance(20)
        
        # Assert
        self.assertEqual(120, round(self.bank_account.balance, 2))

    def test_update_balance_negative_input_updates_balance_correctly(self):

        # Act
        self.bank_account.update_balance(-20)

        # Assert
        self.assertEqual(80, round(self.bank_account.balance, 2))

    def test_update_balance_does_not_change_balance_non_numeric_input(self):

        # Act
        actual = self.bank_account.update_balance("INVALID")

        # Assert
        self.assertEqual(100, round(actual, 2))

    def test_deposit_updates_balance_valid_input(self):

        # Act
        self.bank_account.deposit(20)
        # Assert
        self.assertEqual(self.bank_account.balance, 120)

    def test_deposit_raises_valueerror_negative_input(self):

        # Assert
        with self.assertRaises(ValueError):
            self.bank_account.deposit(-20)

    def test_withdraw_updates_balance_valid_input(self):

        # Act
        self.bank_account.withdraw(20)

        # Assert
        self.assertEqual(self.bank_account.balance, 80)

    def test_withdraw_raises_valueerror_negative_input(self):

        # Assert
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(-20)

    def test_withdraw_amount_exceeds_balance(self):

        # Assert
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(1000)

    def test_str_valid_object_returns_expected_string(self):

        # Arrange
        expected = "Account Number: 20 Balance: $100.00\n"
        actual = str(BankAccount(20, 40, 100))

        # Assert
        self.assertEqual(expected, actual)
