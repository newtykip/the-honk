class Item:
  # Constructor
  def __init__(self, name, description, price, quantity):
    self.name = name
    self.description = description
    self.price = price
    self.initialQuantity = quantity
    self.quantity = quantity