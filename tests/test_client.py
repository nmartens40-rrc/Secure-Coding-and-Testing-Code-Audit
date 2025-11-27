"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

__author__ = "Nick Martens"
__version__ = "1.0.1"
__credits__ = ""


import unittest
from client.client import Client
from email_validator import EmailNotValidError

class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client(20, "Nick", "Martens", "nmartens40@rrc.ca")


    def test_init_attributes_set_to_input_values(self):

        # Arrange
        client_number = 20
        first = "Nick"
        last = "Martens"
        email = "nmartens40@rrc.ca"

        # Assert
        self.assertEqual(client_number, self.client._Client__client_number)
        self.assertEqual(first, self.client._Client__first_name)
        self.assertEqual(last, self.client._Client__last_name)
        self.assertEqual(email, self.client._Client__email_address)

    def test_init_exception_raised_from_invalid_client_number(self):

        # Assert
        with self.assertRaises(ValueError):
            Client("20", "Nick", "Martens", "nmartens40@rrc.ca")

    def test_init_exception_raised_from_blank_first_name(self):

        # Assert
        with self.assertRaises(ValueError):
            Client(20, "", "Martens", "nmartens40@rrc.ca")

    def test_init_exception_raised_from_blank_last_name(self):

        # Assert
        with self.assertRaises(ValueError):
            Client(20, "Nick", "", "nmartens40@rrc.ca")

    def test_init_exception_raised_from_invalid_email_address(self):

        # Act
        output = Client(20, "Nick", "Martens", "")

        # Arrange
        self.assertEqual(output.email_address, "email@pixell-river.com")

    def test_client_number_accessor_returns_client_number_attribute(self):

        # Assert
        self.assertEqual(self.client.client_number, 20)

    def test_first_name_accessor_returns_first_name_attribute(self):

        # Assert
        self.assertEqual(self.client.first_name, "Nick")

    def test_last_name_accessor_returns_last_name_attribute(self):

        # Assert
        self.assertEqual(self.client.last_name, "Martens")

    def test_email_address_accessor_returns_email_address_attribute(self):

        # Assert
        self.assertEqual(self.client.email_address, "nmartens40@rrc.ca")

    def test_str_returns_string_in_expected_format(self):
        
        # Arrange
        expected = "Martens, Nick, [20] - nmartens40@rrc.ca"

        # Act
        actual = str(Client(20, "Nick", "Martens", "nmartens40@rrc.ca"))

        # Assert
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
