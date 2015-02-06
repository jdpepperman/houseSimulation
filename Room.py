class Room(object):
	def __init__(self, house, name):
		self.name = name
		self.house = house
		self.connections = []
		self.actorsInRoom = []

		self.house.addRooms([self])

	def __str__(self):
		s = "Room: " + self.name + "\n"
		s = s + "Connections: "
		for connection in self.connections:
			s = s + connection.name + ", "
		s = s[:-2]

		s = s + "\nActors in Room: \n"
		for actor in self.actorsInRoom:
			s = s + actor.name + ", "
		s = s[:-2]
		return s

	def addConnections(self, listOfRoomsThisConnectsTo):
		for connection in listOfRoomsThisConnectsTo:
			self.connections.append(connection)
			connection.connections.append(self)

	def addActor(self, actor):
		for r in self.house:
			if actor in r.actorsInRoom:
				r.actorsInRoom.remove(actor)
		self.actorsInRoom.append(actor)

	def getConnections(self):
		return self.connections
