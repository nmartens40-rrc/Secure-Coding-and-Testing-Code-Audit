__author__ = "Nick Martens"
__version__ = "1.0.0"
__credits__ = ""

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    An abstract class to handle polymorphism in the update method.
    """

    @abstractmethod
    def update(self, message: str):
        """
        An abstract method used to send alert messages to an email.

        Args:
            message (str): The alert message as a string.
            
        """
        pass