from room import Room
from player import Player
from item import Item

# Declare Items
item = {
    "dagger": Item("dagger", "Short, but to the point"),
    "buckler": Item("buckler", "Can block some attacks")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",["buckler"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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

# set player and start location

player = Player(room['outside'], [])

# Declare defaults
playing = True
action = ''
local_items = Room(player.current_room.name, player.current_room.description, player.current_room.items).items

# main interpreter

while playing is True:
    print(f"========== {player.current_room.name} ==========")
    print(player.current_room.description)
    if player.current_room.items:
        print(f"There are items here.")
        print(local_items)
        print("     (take/drop [item])")
    print("what do you do?")
    action = input("-")
    print("================================================")

    if (action == 'quit'):
        print("Thanks for playing!")
        playing = False
    elif (action == 'help'):
        print("Choose a direction(n,s,e,w)\n take [item], drop [item]\n view inventory (i), or quit")
    elif (action == 'i'):
        print("--Inventory--")
        print(player.items)
    elif (action == 'n'):
        print("Proceeding north...")
        try:
            player.current_room = player.current_room.n_to
        except AttributeError:
            print("The way is blocked...")
    elif (action == 's'):
        print("Proceeding south...")
        try:
            player.current_room = player.current_room.s_to
        except AttributeError:
            print("The way is blocked...")
    elif (action == 'e'):
        print("Proceeding east...")
        try:
            player.current_room = player.current_room.e_to
        except AttributeError:
            print("The way is blocked...")
    elif (action == 'w'):
        print("Proceeding west...")
        try:
            player.current_room = player.current_room.w_to
        except AttributeError:
            print("The way is blocked...")

    for item in local_items:
        if action == f"take {item}":
            print(f"You got {item}")
            player.take_item(item)

    for item in player.items:
        if action == f"drop {item}":
            print(f"\n You lost the {item}")
            player.drop_item(item)


print("================================================")





#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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