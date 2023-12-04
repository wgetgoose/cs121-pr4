class World():
    def __init__(self):
        self.rooms = []
        self.id = -1
    def newID(self):
        self.id += 1
        return self.id
    def register(self, room):
        self.rooms.append(room)
    