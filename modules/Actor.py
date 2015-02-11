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
				r.removeActor(self)
		room.addActor(self)
				
	def getRoom(self):
		for room in self.house:
			if self in room.actorsInRoom:
				return room

        #Moves an actor to a room. If the room is not enterable, they will stay in
        #the same room.
	def moveToRoom(self, room):
		#print(self.name +" moving from " + self.getRoom().name + " to " + room.name)
		from Room import Room
                if room.canEnter == False:
                    room = self.getRoom()
		self.getRoom().removeActor(self)
		room.addActor(self)
