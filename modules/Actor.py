class Actor(object):
	def __init__(self, house, name):
		self.name = name
		self.house = house
		self.house.actors.append(self)
		self.status = "nothing"

	def __str__(self):
		return self.name

	def tick(self):
		pass
	
	def putInRoom(self, room):
		from Room import Room
		for r in self.house:
			if self in r.actorsInRoom:
				r.actorsInRoom.remove(self)
		room.addActor(self)
				
	def getRoom(self):
		for room in self.house:
			if self in room.actorsInRoom:
				return room

	def moveToRoom(self, room):
		from Room import Room
		self.getRoom().actorsInRoom.remove(self)
		room.addActor(self)
