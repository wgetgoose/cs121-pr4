import os

def clear():
    # clear shell commands dependent in windows or not windows
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.loc = None
    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")
    def putInRoom(self, room):
        self.loc = room
        room.addItem(self)
