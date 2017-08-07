from Actor import Actor
from Room import Room
import random


class Person(Actor):
    def __init__(self, house, name, age):
        Actor.__init__(self, house, name)
        self.house.placePersonInRoom(self)
        self.age = age
        self.goingToRoom = None
        self.minuteCount = 0
        self.hunger = random.randint(0, 20)
        self.bathroomNeed = random.randint(0, 10)
        self.travelPath = []

        self.printFlag = False

    def __str__(self):
        s = "Name: " + self.name + "\n"
        s = s + "Age: " + str(self.age) + "\n"
        s = s + "\n"

        return s

    def tick(self):
        self.calcAge()
        self.alterStats()

        if self.status == "eating":
            self.eat()
        elif self.status == "pooping":
            self.poop()
        else:
            if self.__hungry():
                self.eat()
            elif self.__bathroom():
                self.poop()
            else:
                self.wander()

    def __hungry(self):
        return self.hunger >= random.randint(75,
                                             100) or self.hunger > 100 or self.status == "eating" or self.status == "moving to Kitchen"

    def __bathroom(self):
        # self.printFlag = True
        return self.bathroomNeed >= random.randint(75,
                                                   100) or self.bathroomNeed > 100 or self.status == "pooping" or self.status == "moving to Bathroom"

    def wander(self):
        """Makes the person randomly pick a room that he can go to (including the one he's in) and go there"""
        self.status = "wandering"
        possibleRoomsToGoTo = []
        possibleRoomsToGoTo.append(self.getRoom())
        possibleRoomsToGoTo.extend(self.getRoom().getConnections())

        roomToGoTo = possibleRoomsToGoTo[random.randint(0, len(possibleRoomsToGoTo) - 1)]
        self.moveToRoom(roomToGoTo)

    def moveTowardRoomType(self, roomType):
        """Makes the person move in the direction of a room of type roomType. If one is not present in the house, he will wander instead."""
        # if we're looking for a specific Room
        if isinstance(roomType, Room):
            if roomType in self.house.getRooms():
                self.status = "moving to " + type(roomType).__name__
                from Bathroom import Bathroom
                from Kitchen import Kitchen
                currentRoom = self.getRoom()
                # traverse the graph and look for a path. then move along it
                self.fprint(self.name + " is " + "In room: " + currentRoom.name)
                roomToGoTo = self.__getRoomTowardRoomType(roomType)
                self.moveToRoom(roomType)
            else:
                self.wander()
        # if we're looking for a room type
        else:
            if self.house.hasRoomType(roomType):
                self.status = "moving to " + roomType.__name__
                from Bathroom import Bathroom
                from Kitchen import Kitchen
                currentRoom = self.getRoom()
                # traverse the graph and look for a path. then move along it
                self.fprint(self.name + " is " + "In room: " + currentRoom.name)
                roomToGoTo = self.__getRoomTowardRoomType(roomType)
                self.moveToRoom(roomToGoTo)
            else:
                self.wander()

    def __getRoomTowardRoomType(self, roomType):
        # if we're looking for a specific Room
        if isinstance(roomType, Room):
            self.connected = False

            def isConnected(r, rt):
                toCheck = r.getConnections()
                roomCheckedStatus[r] = True
                self.fprint(self.name + " is " + "\tIs " + r.name + " connected to " + rt.name + "?")
                for rm in toCheck:
                    self.fprint(self.name + " is " + "\t\tChecking " + rm.name)
                    if roomCheckedStatus[rm] == False:
                        if rm == rt:
                            self.fprint(self.name + " is " + "True")
                            self.connected = True
                        else:
                            isConnected(rm, rt)
                return self.connected

            # set up the checked status of each room in the house
            roomCheckedStatus = {}
            for room in self.house.getRooms():
                roomCheckedStatus[room] = False

            fromRoom = self.getRoom()
            roomCheckedStatus[fromRoom] = True
            for room in fromRoom.getConnections():
                roomCheckedStatus[room] = True
                if room == roomType:
                    if room.canEnter:
                        return room
                    else:
                        # return self.__getRoomTowardRoomType(type(roomGoingTo))
                        self.wander()
                elif isConnected(room, roomType):
                    return room
        # if we're looking for a room type
        else:
            self.connected = False

            def isConnected(r, rt):
                toCheck = r.getConnections()
                roomCheckedStatus[r] = True
                self.fprint(self.name + " is " + "\tIs " + r.name + " connected to " + rt.__name__ + "?")
                for rm in toCheck:
                    self.fprint(self.name + " is " + "\t\tChecking " + rm.name)
                    if roomCheckedStatus[rm] == False:
                        if isinstance(rm, rt):
                            self.fprint(self.name + " is " + "True")
                            # make this the room we go to no matter what now
                            self.goingToRoom = rm
                            self.connected = True
                        else:
                            isConnected(rm, rt)
                return self.connected

            # set up the checked status of each room in the house
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
            self.hunger = self.hunger - random.randint(1, 4)
            if self.hunger < random.randint(0, 20):
                self.status = "idle"
        else:
            if self.goingToRoom == None:
                self.moveTowardRoomType(Kitchen)
            else:
                self.moveTowardRoomType(self.goingToRoom)

    def poop(self):
        from Bathroom import Bathroom
        if isinstance(self.getRoom(), Bathroom):
            self.status = "pooping"
            self.bathroomNeed = self.bathroomNeed - random.randint(7, 14)
            if self.bathroomNeed < random.randint(0, 7):
                self.status = "idle"
        else:
            if self.goingToRoom == None:
                self.moveTowardRoomType(Bathroom)
            else:
                self.moveTowardRoomType(self.goingToRoom)

    def calcAge(self):
        self.minuteCount = self.minuteCount + 1
        if self.minuteCount >= 525949:
            self.age = self.age + 1
            self.minuteCount = 0

    def setAge(self, age):
        self.age = age

    def alterStats(self):
        if self.status == "idle":
            self.goingToRoom = None

        incHunger = random.randint(0, 100)
        if incHunger < 25:
            self.hunger = self.hunger + 1

        incBathroom = random.randint(0, 100)
        # use this to subtract something to do with how hungry they are
        # ...somehow they need to have to go more if they've eaten recently
        incBathroom = incBathroom - 0
        if incHunger < 25:
            self.bathroomNeed = self.bathroomNeed + 1

    def fprint(self, string):
        if self.printFlag:
            print(string)
