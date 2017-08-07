class Room(object):
    def __init__(self, house, name):
        self.name = name
        self.house = house
        self.connections = []
        self.actorsInRoom = []

        self.connectionNorth = None
        self.connectionSouth = None
        self.connectionEast = None
        self.connectionWest = None

        self.house.addRooms([self])
        self.canEnter = True

    def __str__(self):
        s = "Room: " + self.name + "\n"
        s = s + "Connections: "
        for connection in self.connections:
            s = s + connection.name + ", "
        s = s[:-2]

        s = s + "\nActors in Room: \n"
        if len(self.actorsInRoom) == 0:
            s = s + "\n"
            s = s[:-1]
        else:
            for actor in self.actorsInRoom:
                s = s + actor.name + ", "
            s = s[:-2]
        return s

    # def getDictionary(self):
    #     returnDict = {
    #         'name' : self.name,
    #         'connectionNorth' : self.connectionNorth.name,
    #         'connectionSouth' : self.connectionSouth.name,
    #         'connectionEast' : self.connectionEast.name,
    #         'connectionWest' : self.connectionWest.name,
    #     }

    def addConnection(self, connecting_room, direction):
        self.connections.append(connecting_room)
        connecting_room.connections.append(self)

        if direction == 'N':
            self.connectionNorth = connecting_room
            connecting_room.connectionSouth = self
        elif direction == 'S':
            self.connectionSouth = connecting_room
            connecting_room.connectionNorth = self
        elif direction == 'W':
            self.connectionWest = connecting_room
            connecting_room.connectionEast = self
        elif direction == 'E':
            self.connectionEast = connecting_room
            connecting_room.connectionWest = self
        else:
            print('Invalid direction. Exiting.')
            exit(1)

    def addActor(self, actor):
        from Person import Person
        if isinstance(actor, Person):
            for r in self.house:
                if actor in r.actorsInRoom:
                    r.removeActor(actor)
            if self.canEnter:
                self.actorsInRoom.append(actor)
        else:
            self.actorsInRoom.append(actor)

    def removeActor(self, actor):
        self.actorsInRoom.remove(actor)

    def getConnections(self):
        return self.connections

    def getConnectionNames(self):
        names = []
        for s in self.connections:
            names.append(s.name)

        return names
