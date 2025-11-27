__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Nick Martens"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """

    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
            
        """
        super().__init__()

        if isinstance(account, BankAccount):
            self.__selected_account = copy.deepcopy(account)

        self.account_number_label.setText(f"{self.__selected_account.account_number}")
        self.balance_label.setText(f"${self.__selected_account.balance:,.2f}")

        self.deposit_button.clicked.connect(self.__on_apply_transaction)
        self.withdraw_button.clicked.connect(self.__on_apply_transaction)
        self.exit_button.clicked.connect(self.__on_exit)

    @Slot()
    def __on_apply_transaction(self):
        """
        When a transaction is requested this method determines if the
            user wants to deposit or withdraw then updates the text and
            emits a signal.

        """
        try:
            transaction_amount = float(self.transaction_amount_edit.text())
        except:
            QMessageBox.information(self, "Invalid Data", 
                                    "Amount must be numeric.")
            self.transaction_amount_edit.setFocus()
            return

        try:
            transaction = self.sender()
            transaction_type = "Unknown"

            if transaction not in (self.deposit_button, self.withdraw_button):
                raise ValueError("Unknown transaction type.")
            
            if transaction == self.deposit_button:
                transaction_type = "Deposit"
                self.__selected_account.deposit(transaction_amount)

            elif transaction == self.withdraw_button:
                transaction_type = "Withdraw"
                self.__selected_account.withdraw(transaction_amount)
            
            self.balance_label.setText(f"${self.__selected_account.balance:,.2f}")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

            self.balance_updated.emit(self.__selected_account)
        except Exception as e:
            QMessageBox.information(self, f"{transaction_type} Failed", f"{e}")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()
        

    @Slot()
    def __on_exit(self):
        """
        Closes the accounts details window when the exit button is
            pressed.

        """
        self.close()
