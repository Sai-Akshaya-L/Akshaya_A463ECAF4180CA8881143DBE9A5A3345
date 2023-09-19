class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
  def deposit(self ,amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited ₹{}, New Balance ={}".format(amount,self.__account_balance))
    
    else:
      print("Invalid deposit amount, please enter positive amount")
  def withdraw(self ,amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("withdrawn ₹{}, New Balance = ₹{}".format(amount,self.__account_balance))
    
    else:
      print("Invalid withdrawal amount or insufficient balance") 
  def display_balance(self):
    print("account balance for {} (account #{}): ₹{}".format(self.__account_holder_name, self.__account_number, self.__account_balance))

account = BankAccount(account_number= "123098", account_holder_name = "jaya", initial_balance= 300000.0)

account.display_balance()
account.deposit(12900.0)
account.withdraw(1000.0)
account.display_balance()
