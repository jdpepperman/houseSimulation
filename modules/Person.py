from Actor import Actor
from Room import Room
import random

class Person(Actor):
	def __init__(self, house, name, age):
		Actor.__init__(self, house, name)
		self.house.placePersonInRoom(self)
		self.age = age
		self.minuteCount = 0
		self.hunger = random.randint(0,20)

	def __str__(self):
		s = "Name: " + self.name + "\n"
		s = s + "Age: " + str(self.age) + "\n"
		s = s + "\n"

		return s
		
	def tick(self):
		self.calcAge()
		self.alterStats()
                if self.__hungry():
			self.eat()
		else:
			self.wander()

        def __hungry(self):
            return self.hunger >= random.randint(70,101) or self.hunger > 100 or self.status == "eating" or self.status == "moving to Kitchen"

	def wander(self):
		self.status = "wandering"
		possibleRoomsToGoTo = []
		possibleRoomsToGoTo.append(self.getRoom())
		possibleRoomsToGoTo.extend(self.getRoom().getConnections())

		roomToGoTo = possibleRoomsToGoTo[random.randint(0,len(possibleRoomsToGoTo)-1)]
		self.moveToRoom(roomToGoTo)

        def moveTowardRoomType(self, roomType):
            if self.house.hasRoomType(roomType):
                self.status = "moving to " + roomType.__name__
                from Bathroom import Bathroom
                from Kitchen import Kitchen
                currentRoom = self.getRoom()
                #traverse the graph and look for a path. then move along it
                for room in currentRoom.getConnections():
                    if isinstance(room, roomType):
                        self.moveToRoom(room)
                    else:
			#look through them here!!!!!!!!!!!!!!!!!!!!!!!!!!!
            else:
                self.wander()

	
	def eat(self):
		from Kitchen import Kitchen
		if isinstance(self.getRoom(), Kitchen):
			self.status = "eating"
			self.hunger = self.hunger - random.randint(1,4)
			if self.hunger < random.randint(0,20):
				self.status = "idle"
		else:
			self.moveTowardRoomType(Kitchen)

	def calcAge(self):
		self.minuteCount = self.minuteCount + 1
		if self.minuteCount >= 525949:
			self.age = self.age + 1
			self.minuteCount = 0

	def setAge(self, age):
		self.age = age

	def alterStats(self):
		incHunger = random.randint(0,100)
		if incHunger < 25:
			self.hunger = self.hunger + 1
