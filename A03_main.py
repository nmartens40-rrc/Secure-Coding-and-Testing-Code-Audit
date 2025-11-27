"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Nick Martens"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client

from bank_account import *
from datetime import date
from client.client import Client




# 2. Create a Client object with data of your choice.
try:
    client = Client(1, "Nick", "Martens", "nmartens40@rrc.ca")
except Exception as e:
    print(e)

# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
try:
    account_chequing = ChequingAccount(1, 1, 60, date.today(), 20, 1)
except Exception as e:
    print(e)

try:
    account_savings = SavingsAccount(2, 2, 60, date.today(), 20)
except Exception as e:
    print(e)





# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
account_chequing.attach(client)
account_savings.attach(client)





# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
try:
    client_two = Client(2, "Aiden", "Cameron", "nickym892@gmail.com")
except Exception as e:
    print(e)

try:
    savings_account_two = SavingsAccount(5, 2, 70, date.today(), 20)
except Exception as e:
    print(e)




# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.
try:
    account_chequing.deposit(10000)
except Exception as e:
    print(e)

try:
    account_chequing.withdraw(10060)
except Exception as e:
    print(e)

try:
    account_chequing.deposit(900)
except Exception as e:
    print(e)

try:
    savings_account_two.deposit(10000)
except Exception as e:
    print(e)

try:
    savings_account_two.withdraw(10060)
except Exception as e:
    print(e)

try:
    savings_account_two.deposit(900)
except Exception as e:
    print(e)


try:
    account_savings.deposit(10000)
except Exception as e:
    print(e)

try:
    account_savings.withdraw(10060)
except Exception as e:
    print(e)

try:
    account_savings.deposit(900)
except Exception as e:
    print(e)


