from Person import Person
import random


class House(object):
    def __init__(self):
        self.rooms = []
        self.actors = []

    def __str__(self):
        h = ""
        for room in self.rooms:
            h = h + str(room) + "\n\n"
        return h[:-2]

    def __iter__(self):
        return iter(self.rooms)

    def getDictionary(self):
        returnDict = {}
        for room in self.rooms:
            returnDict[room.name] = room.getDictionary()

        return returnDict

    def getRooms(self):
        return self.rooms

    def placePersonInRoom(self, person):
        for room in self.rooms:
            if person in room.actorsInRoom:
                room.removeActor(person)

        placed = False
        while not placed:
            i = random.randint(0, len(self.rooms) - 1)
            if self.rooms[i].canEnter:
                self.rooms[i].addActor(person)
                placed = True

    def addRooms(self, rooms):
        for room in rooms:
            if room not in self.rooms:
                self.rooms.append(room)

    def hasRoomType(self, roomType):
        for room in self.rooms:
            if isinstance(room, roomType):
                return True

        return False

    def tick(self):
        for actor in self.actors:
            actor.tick()

    def toString_people(self):
        s = "People in house\n[name,\t\tage,\thngr,\tbthrm,\tstatus]:\n"
        for a in self.actors:
            if isinstance(a, Person):
                if len(a.name) < 6:
                    s = s + "[" + a.name + ",\t\t" + str(a.age) + ",\t" + str(a.hunger) + ",\t" + str(
                        a.bathroomNeed) + ",\t" + a.status + "]\n"
                else:
                    s = s + "[" + a.name + ",\t" + str(a.age) + ",\t" + str(a.hunger) + ",\t" + str(
                        a.bathroomNeed) + ",\t" + a.status + "]\n"

        return s
