from Item import Item

class ShoppingBasket:
  # Constructor
  def __init__(self):
    self.items = {} #A dictionary of all the items in the shopping basket: {item:quantity}
    self.checkout = False

  # A method to add an item to the shopping basket
  def addItem(self,item,quantity=1):
    if item.quantity < quantity:
        print(f'Invalid operation - there is not enough {item.name} in stock!')
    elif quantity > 0:
      item.quantity -= quantity
      #Check if the item is already in the shopping basket
      if item in self.items:
        self.items[item] += quantity
      else:
        self.items[item] = quantity
    else:
      print("Invalid operation - Quantity must be a positive number!")

  # A method to remove an item from the shopping basket (or reduce it's quantity)
  def removeItem(self,item,quantity=0):
    if self.items[item] < quantity:
        print(f'Invalid operation - there is not enough {item.name} in the basket!')
    elif quantity<=0:
      #Remove the item
      self.items.pop(item, None)
    else:
      item.quantity += quantity
      if item in self.items:
        if quantity<self.items[item]:
          #Reduce the required quantity for this item
          self.items[item] -= quantity
        else:
          #Remove the item
          self.items.pop(item, None)

  # A method to update the quantity of an item from the shopping basket
  def updateItem(self,item,quantity):
    if quantity > 0:
      quantDifference = self.items[item] if item in self.items else 0
      quantDifference -= quantity
      item.quantity += quantDifference
      self.items[item] = quantity
    else:
      self.removeItem(item)

  # A method to view/list the content of the basket.
  def view(self):
    totalCost = 0
    print("---------------------")
    for item in self.items:
      quantity = self.items[item]
      cost = quantity * item.price
      print(" + " + item.name + " - " + str(quantity) + " x £" + '{0:.2f}'.format(item.price) + " = £" + '{0:.2f}'.format(cost))
      totalCost += cost
    print("---------------------")
    print(" = £" + '{0:.2f}'.format(totalCost))
    print("---------------------")

  # A method to calculate the total cost of the basket.
  def getTotalCost(self):
    totalCost = 0
    for item in self.items:
      quantity = self.items[item]
      cost = quantity * item.price
      totalCost += cost
    return totalCost

  # A method to empty the content of the basket
  def reset(self):
    for item in self.items:
        item.quantity = item.initialQuantity

    self.items = {}

  # A method to return whether the basket is empty or not:
  def isEmpty(self):
    return len(self.items)==0

