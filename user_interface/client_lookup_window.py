__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Nick Martens"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """
    Defines the methods for the client lookup window
    """

    def __init__(self):
        """
        Initializes the super __init__ method and grabs the csv data.
            Also initializes buttons from the lookup window.

        """
        super().__init__()
        self.__data = load_data()
        self.__client_listing = self.__data[0]
        self.__accounts = self.__data[1]
        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)
        self.filter_button.clicked.connect(self.__on_filter_clicked)
    
# Ask Laurie if message boxes count as raises in documentation!!!

    @Slot()
    def __on_lookup_client(self):
        """
        This method is called when the lookup client button is pressed.
            It grabs the client number and the clients info and 
            accounts and puts them in the accounts table.

        """
        try:
            client_number = int(self.client_number_edit.text())
        except Exception as e:
            QMessageBox.information(self, "Input Error", "The client number "
            "must be a numeric value.")
            self.reset_display()
            return

        if client_number not in self.__client_listing.keys():
            QMessageBox.information(self, "Not Found", "Client number: "
            f"{client_number} not found.")
            self.reset_display()
            return
        
        else:
            client = self.__client_listing[client_number]
            self.client_info_label.setText(f"Client Name: {client.first_name}"
                                           f" {client.last_name}")

            for accounts in self.__accounts.values():
                if accounts.client_number == client_number:

                    balance = f"${accounts.balance:,.2f}"
                    self.account_table.insertRow(0)

                    account_number_item = QTableWidgetItem(
                        str(accounts.account_number))
                    account_number_item.setTextAlignment(Qt.AlignCenter)

                    balance_item = QTableWidgetItem(balance)
                    balance_item.setTextAlignment(Qt.AlignCenter)

                    date_created_item = QTableWidgetItem(
                        str(accounts._date_created))
                    date_created_item.setTextAlignment(Qt.AlignCenter)

                    class_name_item = QTableWidgetItem(
                        str(accounts.__class__.__name__))
                    class_name_item.setTextAlignment(Qt.AlignCenter)

                    self.account_table.setItem(0, 0, 
                            account_number_item)
                    
                    self.account_table.setItem(0, 1, 
                            balance_item)
                    
                    self.account_table.setItem(0, 2, 
                            date_created_item)
                    
                    self.account_table.setItem(0, 3, 
                            class_name_item)
                    self.__toggle_filter(False)
                    
            self.account_table.resizeColumnsToContents()
                    
    @Slot()  
    def __on_text_changed(self):
        """
        This method clears the table when the client lookup text is
            changed.

        """
        self.account_table.setRowCount(0)

    @Slot()
    def __on_select_account(self):
        """
        This method grabs the account information from the selected
            row and opens a window to interact with that account if
            the selected account is valid.

        """
        selected_row = self.account_table.currentRow()
        account_number = self.account_table.item(selected_row, 0).text()

        if account_number.strip() == "":
            QMessageBox.information(self, "Invalid Selection", 
                                    "Please select a valid record.")
        
        account_number = int(account_number)

        if account_number in self.__accounts:
            account = self.__accounts[account_number]
            selected_account = AccountDetailsWindow(account)
            selected_account.balance_updated.connect(self.__update_data)

            selected_account.exec()
        else:
            QMessageBox.information(self, "Not Found", "Bank account selected"
            "does not exist.")

    @Slot()
    def __update_data(self, account: BankAccount):
        """
        Args:
            account (BankAccount): The account instance that needs to
                be updated.
        
        Updates the correct rows balance when a change is made.

        """
        account_number = account.account_number

        for row in range(self.account_table.rowCount()):
            if int(self.account_table.item(row, 0).text()) == account_number:
                self.account_table.item(row, 1).setText\
                (f"${account.balance:,.2f}")
        
        self.__accounts[account_number] = account
        update_data(account)

    @Slot()
    def __on_filter_clicked(self):
        """
        When the filter button is clicked, this method checks the value
            of the filter button's text and either filters the data by
            grabbing the filter edit's text or resets the filter
            depending on the text of the filter button.

        """
        if self.filter_button.text() == "Apply Filter":
            filter_index = self.filter_combo_box.currentIndex()
            filter_text = self.filter_edit.text()

            for row in range(self.account_table.rowCount()):
                record = self.account_table.item(row, filter_index)
                if record.text().lower() and filter_text not in record.text().lower():
                    self.account_table.setRowHidden(row, True)
                    self.__toggle_filter(True)
        else:
            self.__toggle_filter(False)

    def __toggle_filter(self, filter_on: bool):
        """
        Args:
            filter_on (bool): A boolean value representing if a search
                filter is currently applied.

        When this method receives a value of true it changes the text
            of the filter button to reset and disables input fields
            until the filter is reset and also sets the text in the
            filter label to show that the data is filtered. If the
            method receives a value of false it changes the text of the
            filter button and enables input fields so they can receive
            filter instructions and also reveals all hidden rows.
            
        """
        self.filter_button.setEnabled(True)
        if filter_on == True:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setDisabled(True)
            self.filter_edit.setDisabled(True)
            self.filter_label.setText("Data is Currently Filtered")
        elif filter_on == False:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)
            self.filter_label.setText("Data is Not Currently Filtered")
                

