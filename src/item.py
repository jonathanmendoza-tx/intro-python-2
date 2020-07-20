class Item:
	def __init__(self, name, description, found = False):
		self.name = name
		self.description = description
		self.found = found

	def __str__(self):
		return f'--{self.name}-- '

class Weapon(Item):
	def __init__(self, name, description, found, damage):
		super().__init__(name, description, found)
		self.damage = damage

	def __str__(self):
		return super().__str__() + f'{self.damage} damage'
	

class Utility(Item):
	def __init__(self, name, description, found, uses):
		super().__init__(name, description, found)
		self.uses = uses

	def __str__(self):
		return super().__str__() + f'{self.uses} uses left'
	