class Room(object):
    def __init__(self, house, name):
        self.name = name
        self.house = house
        self.connections = []
        self.actors_in_room = []

        self.connection_north = None
        self.connection_south = None
        self.connection_east = None
        self.connection_west = None

        self.house.addRooms([self])
        self.can_enter = True

    def __str__(self):
        string = "Room: " + self.name + "\n"
        string = string + "Connections: "
        for connection in self.connections:
            string = string + connection.name + ", "
        string = string[:-2]

        string = string + "\nActors in Room: \n"
        num_actors_in_room = len(self.actors_in_room)
        if num_actors_in_room == 0:
            string = string + "\n"
            string = string[:-1]
        else:
            for actor in self.actors_in_room:
                string = string + actor.name + ", "
            string = string[:-2]
        return string

    def getDictionary(self):
        return_dict = {}

        connections_dict = {}
        if self.connection_north is not None:
            connections_dict['connection_north'] = self.connection_north.name
        if self.connection_south is not None:
            connections_dict['connection_south'] = self.connection_south.name
        if self.connection_east is not None:
            connections_dict['connection_east'] = self.connection_east.name
        if self.connection_west is not None:
            connections_dict['connection_west'] = self.connection_west.name
        num_connections = len(connections_dict.values())
        if num_connections > 0:
            return_dict['Connections'] = connections_dict
        num_actors_in_room = len(self.actors_in_room)
        if num_actors_in_room > 0:
            actors_dict = {}

            for actor in self.actors_in_room:
                actors_dict[actor.name] = actor.getDictionary()

            return_dict['Actors'] = actors_dict

        return return_dict

    def addConnection(self, connecting_room, direction):
        self.connections.append(connecting_room)
        connecting_room.connections.append(self)

        if direction == 'N':
            self.connection_north = connecting_room
            connecting_room.connection_south = self
        elif direction == 'S':
            self.connection_south = connecting_room
            connecting_room.connection_north = self
        elif direction == 'W':
            self.connection_west = connecting_room
            connecting_room.connection_east = self
        elif direction == 'E':
            self.connection_east = connecting_room
            connecting_room.connection_west = self
        else:
            print('Invalid direction. Exiting.')
            exit(1)

    def addActor(self, actor):
        from modules.Person import Person
        if isinstance(actor, Person):
            for room in self.house:
                if actor in room.actors_in_room:
                    room.removeActor(actor)
            if self.can_enter:
                self.actors_in_room.append(actor)
        else:
            self.actors_in_room.append(actor)

    def removeActor(self, actor):
        self.actors_in_room.remove(actor)

    def getConnections(self):
        return self.connections

    def getConnectionNames(self):
        names = []
        for conn in self.connections:
            names.append(conn.name)

        return names
