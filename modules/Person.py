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
                self.bathroomNeed = random.randint(0,10)

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
                elif self.__bathroom():
                    self.poop()
		else:
			self.wander()

        def __hungry(self):
            return self.hunger >= random.randint(75,100) or self.hunger > 100 or self.status == "eating" or self.status == "moving to Kitchen"

        def __bathroom(self):
            return self.bathroomNeed >= random.randint(75,100) or self.bathroomNeed > 100 or self.status == "pooping" or self.status == "moving to Bathroom"

	def wander(self):
                """Makes the person randomly pick a room that he can go to (including the one he's in) and go there"""
		self.status = "wandering"
		possibleRoomsToGoTo = []
		possibleRoomsToGoTo.append(self.getRoom())
		possibleRoomsToGoTo.extend(self.getRoom().getConnections())

		roomToGoTo = possibleRoomsToGoTo[random.randint(0,len(possibleRoomsToGoTo)-1)]
		self.moveToRoom(roomToGoTo)

        def moveTowardRoomType(self, roomType):
            """Makes the person move in the direction of a room of type roomType. If one is not present in the house, he will wander instead."""
            if self.house.hasRoomType(roomType):
                self.status = "moving to " + roomType.__name__
                from Bathroom import Bathroom
                from Kitchen import Kitchen
                currentRoom = self.getRoom()
                #traverse the graph and look for a path. then move along it
                print("In room: " + currentRoom.name)
                roomToGoTo = self.__getRoomTowardRoomType(roomType)
                self.moveToRoom(roomToGoTo)
            else:
                self.wander()

        def __getRoomTowardRoomType(self, roomType):
            self.connected = False
            def isConnected(r, rt):
                toCheck = r.getConnections()
                roomCheckedStatus[r] = True
                print("\tIs " + r.name + " connected to " + rt.__name__ + "?")
                for rm in toCheck:
                    print("\t\tChecking " + rm.name)
                    if roomCheckedStatus[rm] == False:
                        if isinstance(rm, rt):
                            print("True")
                            self.connected = True
                        else:
                            isConnected(rm, rt)
                return self.connected
            
            #set up the checked status of each room in the house
            roomCheckedStatus = {}
            for room in self.house.getRooms():
                roomCheckedStatus[room] = False
            
            fromRoom = self.getRoom()
            roomCheckedStatus[fromRoom] = True
            for room in fromRoom.getConnections():
                roomCheckedStatus[room] = True
                if isinstance(room, roomType) or isConnected(room, roomType):
                    return room

	def eat(self):
		from Kitchen import Kitchen
		if isinstance(self.getRoom(), Kitchen):
			self.status = "eating"
			self.hunger = self.hunger - random.randint(1,4)
			if self.hunger < random.randint(0,20):
				self.status = "idle"
		else:
			self.moveTowardRoomType(Kitchen)

        def poop(self):
            from Bathroom import Bathroom
            if isinstance(self.getRoom(), Bathroom):
                self.status = "pooping"
                self.bathroomNeed = self.bathroomNeed - random.randint(7,14)
                if self.bathroomNeed < random.randint(0,7):
                    self.status = "idle"
            else:
                self.moveTowardRoomType(Bathroom)

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

                incBathroom = random.randint(0,100)
                #use this to subtract something to do with how hungry they are
                #...somehow they need to have to go more if they've eaten recently
                incBathroom = incBathroom - 0
                if incHunger < 25:
                    self.bathroomNeed = self.bathroomNeed + 1
