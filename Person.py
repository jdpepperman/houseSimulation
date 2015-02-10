from Actor import *
import random

class Person(Actor):
	def __init__(self, house, name, age):
		Actor.__init__(self, house, name)
		self.house.placePersonInRoom(self)
		self.age = age
		self.hourCount = 0
		self.hunger = random.randint(0,20)

	def __str__(self):
		s = "Name: " + self.name + "\n"
		s = s + "Age: " + str(self.age) + "\n"
		s = s + "\n"

		return s
		
	def tick(self):
		self.calcAge()
		self.wander()
		self.alterStats()

	def wander(self):
		self.status = "wandering"
		possibleRoomsToGoTo = []
		possibleRoomsToGoTo.append(self.getRoom())
		possibleRoomsToGoTo.extend(self.getRoom().getConnections())

		roomToGoTo = possibleRoomsToGoTo[random.randint(0,len(possibleRoomsToGoTo)-1)]
		self.moveToRoom(roomToGoTo)
	
	def calcAge(self):
		self.hourCount = self.hourCount + 1
		if self.hourCount >= 8766:
			self.age = self.age + 1
			self.hourCount = 0

	def setAge(self, age):
		self.age = age

	def alterStats(self):
		incHunger = random.randint(0,4)
		if incHunger == 0:
			self.hunger = self.hunger + 1
