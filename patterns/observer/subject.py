__author__ = "Nick Martens"
__version__ = "1.0.0"
__credits__ = ""

from abc import ABC, abstractmethod
from .observer import Observer

class Subject(ABC):
    """
    Defines methods to handle alert messages.
    """

    def __init__(self):
        """
        Declares the observers list. 
        """
        self._observers = []

    @abstractmethod
    def attach(self, observer: Observer):
        """
        Attaches the observer to the observers list.

        Args:
            observer (Observer): A variable storing an observer.

        """
        pass
    
    @abstractmethod
    def detach(self, observer: Observer):
        """
        Detaches an observer from the observers list.

        Args:
            observer (Observer): A variable storing an observer.

        """
        pass
    
    @abstractmethod
    def notify(self, message: str):
        """
        Sends all the observer messages to the update method in the
            subject class to be sent to an email.

        Args:
            observer (Observer): A variable storing an observer.

        """
        pass