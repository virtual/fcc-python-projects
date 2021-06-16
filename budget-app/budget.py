import math
class Category:
  categories = []
  # ledger = []
  # name = ''
  
  # When the budget object is printed it should display:
  # * A title line of 30 characters where the name of the category is centered in a line of `*` characters.
  # * A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
  # * A line displaying the category total.
  # Here is an example of the output:
  # ```
  # *************Food*************
  # initial deposit        1000.00
  # groceries               -10.15
  # restaurant and more foo -15.89
  # Transfer to Clothing    -50.00
  # Total: 923.96
  # ```
  
  def __str__(self):
    output = ''
    for iter in range(len(self.ledger)):
      amount = float(self.ledger[iter]['amount'])
      amtCurrency = str("{:.2f}".format(amount))
      description = (self.ledger[iter]['description'])
      descShort = (description[:23]) if len(description) > 23 else description.ljust(23)
      output = output + "\n" + descShort + ' ' + amtCurrency
    output = output + "\nTotal: " + str(self.get_balance())
    catprint = self.printCategoryTitle(self.name, 30)
    
    return f'{catprint}{output}'


  def __init__(self, category):
    self.categories.append(category)
    self.ledger = []
    self.name = category
    
  ## Center the category title based on length
  def printCategoryTitle(self, title, length):
    catlength = len(title)
    registryWidth = length
    catprint = ''
    char = '*'
    catprint = (math.floor((registryWidth-catlength)/2) * char) 
    catprint = catprint + title + catprint
    if (len(title)%2 == 1):
      catprint += char
    return catprint

  def deposit(self, amount, note = ''):
    line = {"amount": amount, "description": note}
    self.ledger.append(line)
    return True

  def withdraw(self, amount, note = ''):
    if (self.get_balance() >= amount):
      line = {"amount": amount * -1, "description": note}
      self.ledger.append(line)
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
    '''
    Send a message to a recipient

    :param float amount: The amount of money to transfer
    :param str targetCategory: The target category to transfer to
    :return: `True` if the transfer took place, and `False` otherwise
    :rtype: boolean
    '''
    if (self.check_funds(amount)):
      self.withdraw(amount, "Transfer to " + targetCategory.name)
      targetCategory.deposit(amount, "Transfer from " + self.name)
      return True
    
    return False

  # It returns `False` if the amount is greater than the balance of the budget category and returns `True` otherwise. This method should be used by both the `withdraw` method and `transfer` method.
  def check_funds(self, amount=0):
    if (self.get_balance() >= amount):
      return True
    else:
      return False

def create_spend_chart(self, categories =[]):
  '''
  Creates a chart

  :param list categories: list of categories
  :return: bar chart of spending
  :rtype: str

  The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".

+ 100|          
+  90|          
+  80|          
+  70|    o     
+  60|    o     
+  50|    o     
+  40|    o     
+  30|    o     
+  20|    o  o  
+  10|    o  o  
+   0| o  o  o  
+     ----------
+      B  F  E  
+      u  o  n  
+      s  o  t  
+      i  d  e  
+      n     r  
+      e     t  
+      s     a  
+      s     i  
+            n  
+            m  
+            e  
+            n  
+            t  
  '''
  chart = 'Percentage spent by category\n'
  for iter in range(100, 0, -10):
    chart = chart + str(iter).rjust(3, ' ') + '|' + (' '*10) + '\n'
    # print(chart)
  return chart
  #   self.deposit = deposit
  #   self.withdraw = withdraw
  #   self.get_balance = get_balance
  #   self.transfer = transfer
  #   self.check_funds = check_funds