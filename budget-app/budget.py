class Category:
  # categories = ''
  # ledger = []
  
  def __init__(self, categories):
    self.categories = categories
    self.ledger = []
    
  def deposit(self, amount, note = ''):
    line = {"amount": amount, "description": note}
    self.ledger.append(line)
    # print(self.ledger)
    return True

  def withdraw(self, amount, note = ''):
    if (self.get_balance() >= amount):
      line = {"amount": amount * -1, "description": note}
      self.ledger.append(line)
      # print(self.ledger)
      return True
    else:
      return False

  # Read the ledger and return the current balance 
  # after deposits and withdraws
  def get_balance(self):
    total = 0
    for iter in range(len(self.ledger)):
      amount = (float(self.ledger[iter]['amount']))
      total = total + amount
    # print('total:', total)
    return total

  def transfer(self, amount, targetCategory):
    # self.ledger.append('x')
    print(self.ledger)

  # It returns `False` if the amount is greater than the balance of the budget category and returns `True` otherwise. This method should be used by both the `withdraw` method and `transfer` method.
  def check_funds(self, amount=0):
    if (self.get_balance() >= amount):
      return True
    else:
      return False
    # self.ledger.append('x')
    # print(self.ledger)

def create_spend_chart(self, categories =[]):
    # self.ledger.append('x')
    print('100  Mew mew')
      
  #   self.deposit = deposit
  #   self.withdraw = withdraw
  #   self.get_balance = get_balance
  #   self.transfer = transfer
  #   self.check_funds = check_funds