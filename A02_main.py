"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Nick Martens"

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime

from bank_account import *
from datetime import date


# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
try:
    chequing = ChequingAccount(10, 10, 100, date(2024, 5, 15), 150, 0.1)
except Exception as e:
    print(e)


# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(chequing)
print(chequing.get_service_charges())


# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
try:
    chequing.deposit(100)
except Exception as e:
    print(e)
print(chequing)
print(chequing.get_service_charges())


print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
try:
    savings = SavingsAccount(20, 20, 100, date(2024, 5, 15), 50)
except Exception as e:
    print(e)


# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(savings)
print(savings.get_service_charges())


# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
savings.withdraw(99)
print(savings)
print(savings.get_service_charges())


print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
try:
    investment_one = InvestmentAccount(20, 20, 100, date(2024, 5, 15), 5)
except Exception as e:
    print(e)


# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
print(investment_one)
print(investment_one.get_service_charges())


# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
try:
    investment_two = InvestmentAccount(20, 20, 100, date(2014, 5, 15), 5)
except Exception as e:
    print(e)


# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print(investment_two)
print(investment_two.get_service_charges())


print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
try:
    chequing.withdraw(0.5)
except Exception as e:
    print(e)
try:
    savings.withdraw(0.5)
except Exception as e:
    print(e)
try:
    investment_one.withdraw(5.5)
except Exception as e:
    print(e)
try:
    investment_two.withdraw(0.5)
except Exception as e:
    print(e)




# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print(chequing)
print(savings)
print(investment_one)
print(investment_two)
