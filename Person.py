from Actor import *
import random

class Person(Actor):
	def __init__(self, house, name):
		Actor.__init__(self, house, name)
		self.house.placePersonInRoom(self)
		
	def tick(self):
		self.wander()

	def wander(self):
		possibleRoomsToGoTo = []
		possibleRoomsToGoTo.append(self.getRoom())
		possibleRoomsToGoTo.append(self.getRoom().getConnections())

		roomToGoTo = possibleRoomsToGoTo[random.randint(0,len(possibleRoomsToGoTo))]
		self.moveToRoom(roomToGoTo)
