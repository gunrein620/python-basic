class Account:
  def __init__(self):
    self.balance = 0
    
  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    self.balance -= amount

  def get_balance(self):
    return self.balance
  
a1 = Account()
a1.deposit(1000)
a1.withdraw(500)
print(a1.get_balance())

a2 = Account()
a2.deposit(2000)
a2.withdraw(1000)
print(a2.get_balance())
    