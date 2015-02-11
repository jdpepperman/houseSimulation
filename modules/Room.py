class Room(object):
	def __init__(self, house, name):
		self.name = name
		self.house = house
		self.connections = []
		self.actorsInRoom = []

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

	def addConnections(self, listOfRoomsThisConnectsTo):
		for connection in listOfRoomsThisConnectsTo:
			self.connections.append(connection)
			connection.connections.append(self)

	def addActor(self, actor):
		from Person import Person
		if isinstance(actor, Person):
			for r in self.house:
				if actor in r.actorsInRoom:
					r.actorsInRoom.remove(actor)
			if self.canEnter:
				self.actorsInRoom.append(actor)
		else:
			self.actorsInRoom.append(actor)

	def getConnections(self):
		return self.connections
