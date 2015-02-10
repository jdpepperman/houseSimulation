from Room import *

class Bathroom(Room):
	def __init__(self, house, name):
		Room.__init__(self, house, name)
		self.occupied = False
		self.occupiedBy = None

	def addActor(self, actor):
		Room.addActor(self, actor)
		if isinstance(actor, Person):
			self.occupiedBy = actor
			self.occupied = True
			self.canEnter = False
