class World():
    def __init__(self):
        self.rooms = []
        self.day = 0
        self.id = -1
    def newID(self):
        self.id = self.id + 1
        return int(self.id)
