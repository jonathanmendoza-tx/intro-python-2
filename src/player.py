from room import Room
# Write a class to hold player information, e.g. what room they are in
# currently.

class Player(Room):
	def __init__(self, name, room):
		self.name = name
		self.room = room

	def __str__(self):
		return f'{self.name} is currently at the {self.room}'