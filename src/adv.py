from room import Room
from player import Player
from item import *

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 
                     [Utility('Torch','Lights up the darkness', False,  25)]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('player1', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

q = False

while q == False:


	query = input('What would you like to do? (M)ove, (C)heck area, (V)iew inventory:\n').lower()

	query = query.split()

	if query[0] == 'get' and len(query) > 1:

		#check if item exists in current player room and has been found
		room_items = [item.name.lower() for item in player.room.items if item.found == True]

		if query[1] in room_items:
			for ind, item in enumerate(player.room.items):
				if item.name.lower() == query[1]:

					item = player.room.items.pop(ind)

					player.items.append(item)
			

	elif len(query)==1:

		if 'm' in query or 'move' in query :
			print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
			print(player.room)
			print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
			direction = input("Which direction would you like to move? [(N)orth, (E)ast, (S)outh, (W)est, (Q)uit]").lower()
			move = direction[0]+'_to'
			if 'q' in direction:
				q = True

			elif hasattr(player.room, move):
				player.room = getattr(player.room, move)

			else:
				print('---------------------------------------')
				print('----Cannot go that way at this time----')
				print('---------------------------------------')

		elif 'c' in query or 'check' in query:
			print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
			print(f'{player.room.description}\n')
			print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

			if len(player.room.items) > 0:

				print('||You get the feeling there might be something useful nearby.||')

				search = input(f'	Would you like to search the area? [(Y)es, (N)o]\n').lower()

				if 'y' in search or 'yes' in search:

					print(f'You see a {player.room.items[0]}')
					player.room.items[0].found = True

					print("~~~HINT: you can use the command 'get' to grab items and 'drop' to drop them~~~\n")

		elif 'v' in query or 'view' in query or 'inventory' in query:
			print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
			print(f'You currently have {len(player.items)} items:')
			for item in player.items:
				print(item)
			print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

