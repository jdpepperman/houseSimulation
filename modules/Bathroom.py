from Room import Room

class Bathroom(Room):
	def __init__(self, house, name):
		Room.__init__(self, house, name)
		self.occupied = False
		self.occupiedBy = None

	def addActor(self, actor):
		from Person import Person
		Room.addActor(self, actor)
		if isinstance(actor, Person):
			self.occupiedBy = actor
			self.occupied = True
			self.canEnter = False
