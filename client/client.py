__author__ = "Nick Martens"
__version__ = "1.0.1"
__credits__ = ""

from email_validator import validate_email, EmailNotValidError
from patterns.observer.observer import Observer
from abc import abstractmethod
from utility.file_utils import simulate_send_email
from datetime import datetime

class Client(Observer):
    """
    The Client class maintains client data.
    """

    def __init__(self, client_number: int, first_name: str, last_name: str, 
                email_address: str):
        """
        Args:
            client_number (int): An integer value representing 
                the client number.
            first_name (str): A string value representing 
                the clients first name.
            last_name (str): A string value representing the clients
                last name.
            email_address (str): A string value representing the
                clients email address.

        Returns:
            None
        
        Raises:
            ValueError: When the client number isn't numeric, or the
                first or last name is blank.

        """

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be numeric")
        
        if len(first_name.strip()) == 0:
            raise ValueError("First name can't be blank.")
        else:
            self.__first_name = first_name.strip()

        if len(last_name.strip()) == 0:
            raise ValueError("Last name can't be blank.")
        else:
            self.__last_name = last_name.strip()        

        try:
            validate_email(email_address, check_deliverability = False)
            self.__email_address = email_address
        except EmailNotValidError as e:
            self.__email_address = "email@pixell-river.com"

        # Accessors

    @property
    def client_number(self) -> int:
        """
        Accessor for the client number attribute.

        Returns:
            int: The client's bank number.

        """
        return self.__client_number
    
    @property
    def first_name(self) -> str:
        """
        Accessor for the first name attribute.

        Returns:
            str: The clients first name.

        """
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        """
        Accessor for the last name attribute.

        Returns:
            str: The clients last name.

        """
        return self.__last_name
    
    @property
    def email_address(self) -> str:
        """
        Accessor for the email address attribute.

        Returns:
            str: The clients email address.

        """
        return self.__email_address

    def __str__(self):
        """
        Returns a formatted string that includes the client number,
            first and last names, and email address.

        Returns:
            str: A formatted string representation.
            
        """
        return (f"{self.__last_name}, {self.__first_name},"
        f" [{self.__client_number}] - {self.__email_address}")
    
    
    def update(self, message: str):
        """
        This method generates the alert message and subject and sends
            them to the simulate_send_email function to send the alert.
        
        Args:
            message (str): The alert message that gets sent to
                a clients email.
                
        """
        subject = f"ALERT: Unusual Activity: {datetime.today()}"
        alert_message = (f"Notification for {self.__client_number}: "
            f"{self.__first_name} {self.__last_name}: {message}")
        
        simulate_send_email(self.__email_address, subject, alert_message)
        