# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, current_room, items):
        self.current_room = current_room
        self.items = items

    def take_item(self, item):
        self.current_room.items.remove(item)
        self.items.append(item)

    def drop_item(self, item):
        self.current_room.items.append(item)
        self.items.remove(item)