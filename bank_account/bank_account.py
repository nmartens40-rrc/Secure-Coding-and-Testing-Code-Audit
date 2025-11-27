__author__ = "Nick Martens"
__version__ = "1.0.1"
__credits__ = ""

from datetime import date
from abc import ABC, abstractmethod
from patterns.observer.subject import Subject
from patterns.observer.observer import Observer

class BankAccount(Subject, ABC):
    """
    The BankAccount class maintains a client's bank account data.
    """

    def __init__(self, account_number: int, client_number: int, 
                balance: float, date_created: date):
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

        Returns: None

        Raises:
            ValueError: Raised when the account number or client number
                isn't an integer value.
        
        """

        super().__init__()

        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()

        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account number must be an integer")
        
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be an integer")
        
        try:
            float(balance)
            self.__balance = balance
        except:
            self.__balance = 0
        
        self.BASE_SERVICE_CHARGE = 0.50
        self.LARGE_TRANSACTION_THRESHOLD = 9999.99
        self.LOW_BALANCE_LEVEL = 50.0
        


    @property
    def account_number(self) -> int:
        """
        Accessor for the account number attribute.

        Returns:
            int: The client's account number.

        """
        return self.__account_number
    
    @property
    def client_number(self) -> int:
        """
        Accessor for the client number attribute.

        Returns:
            int: The client's bank number.

        """
        return self.__client_number
    
    @property
    def balance(self) -> float:
        """
        Accessor for the balance attribute.

        Returns:
            float: The client balance.

        """
        return self.__balance
    

    def update_balance(self, amount: float):
        """
        Args:
            transaction_amount (float): The desired transaction amount.

        Returns:
            The updated balance.

        Raises:
            ValueError: When the withdraw amount exceeds the account
                balance or when the transaction can't be converted to
                a float.

        """
        
        try:
            float(amount)
        except ValueError:
            return self.__balance
        self.__balance = self.__balance + amount

        if self.__balance < self.LOW_BALANCE_LEVEL:
            message = (f"Low balance warning {self.__balance:,.2f}: "
                f"on account {self.__account_number}")
            self.notify(message)

        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            message = (f"Large Transaction {amount:,.2f}: on account"
                    f" {self.__account_number}")
            self.notify(message)
        
    def deposit(self, amount: float):
        """
        Args:
            deposit_amount (str): The desired deposit amount.

        Returns:
            The updated balance after the deposit.

        Raises:
            ValueError: When the desired amount can't be converted to
                a float or if the amount is less than zero.

        """
        
        try:
            float(amount)
        except ValueError:
            raise ValueError(f"Deposit amount: {amount} "
                            "must be numeric.")
        
        if amount <= 0:
            raise ValueError(f"Deposit amount: {amount:.2f} "
                            "must be positive")
        self.update_balance(amount)
    
    def withdraw(self, amount: float):
        """
        Args:
            withdraw_amount (str): The desired withdraw amount.

        Returns:
            The updated balance after the withdraw.

        Raises:
            ValueError: When the withdraw amount can't be converted to
                a float or when the input isn't positive.
                
        """

        try:
            float(amount)
        except ValueError:
            raise ValueError(f"Withdrawal amount: "
                            f"{amount} must be numeric.")
        
        if amount > 0:
            amount =amount * -1
        else:
            raise ValueError(f"Withdrawal amount:{amount:.2f} "
                            "must be positive")
        if abs(amount) > self.__balance:
                raise ValueError(f"Withdrawal amount: "
                                f"{amount:,.2f} must not exceed"
                                f" the account balance: {self.__balance:,.2f}")
        self.update_balance(amount)
    
    def __str__(self) -> str:
        """
        Returns a formatted string containing the account number and
            the updated balance.

        Returns:
            str: A formatted string representation.

        """

        return (f"Account Number: {self.__account_number} Balance:"
        f" ${self.__balance:,.2f}\n")
    
    @abstractmethod
    def get_service_charges(self) -> float:
        """
        Returns the service charge of the bank account instance.

        Returns:
            float: The bank account's service charge.
        
        """
        pass

    def attach(self, observer: Observer):
        """
        Attaches the observer to the observers list.

        Args:
            observer (Observer): A variable storing an observer.

        """
        self._observers.append(observer)

    def detach(self, observer: Observer):
        """
        Detaches an observer from the observers list.

        Args:
            observer (Observer): A variable storing an observer.

        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str):
        """
        Sends all the observer messages to the update method in the
            subject class to be sent to an email.

        Args:
            observer (Observer): A variable storing an observer.

        """
        for observer in self._observers:
            observer.update(message)
