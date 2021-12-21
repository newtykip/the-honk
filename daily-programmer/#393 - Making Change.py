COINTYPES = [500, 100, 25, 10, 5, 1]

class Change():
	def __init__(self, value):
		self.value = value # Save the value
		self.coins = {} # Create a dictionary for the coins
		curr = value # Make a temporary variable to alter
		for TYPE in COINTYPES: # For each coin type
			index = COINTYPES.index(TYPE) # Get the index
			if index > 0: # If the coin type is not at the first index
				curr = curr % COINTYPES[index - 1] # Work out the remainder
			self.coins[TYPE] = curr // TYPE # And work out how many of the coin type fits into that remainder
		self.total = sum(self.coins.values()) # How many coins are there in total?
		
change = Change(123456)
print(change.coins, change.total)
