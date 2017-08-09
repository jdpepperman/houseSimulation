import random
from Person import Person


class House(object):
    def __init__(self):
        self.rooms = []
        self.actors = []

    def __str__(self):
        house_string = ""
        for room in self.rooms:
            house_string = house_string + str(room) + "\n\n"
        return house_string[:-2]

    def __iter__(self):
        return iter(self.rooms)

    def getDictionary(self):
        return_dict = {}
        for room in self.rooms:
            return_dict[room.name] = room.getDictionary()

        return return_dict

    def getRooms(self):
        return self.rooms

    def placePersonInRoom(self, person):
        for room in self.rooms:
            if person in room.actors_in_room:
                room.removeActor(person)

        placed = False
        while not placed:
            i = random.randint(0, len(self.rooms) - 1)
            if self.rooms[i].can_enter:
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
        string = "People in house\n[name,\t\tage,\thngr,\tbthrm,\tstatus]:\n"
        for actor in self.actors:
            if isinstance(actor, Person):
                if len(actor.name) < 6:
                    string = (string + "[" + actor.name + ",\t\t" + str(actor.age) + ",\t" +
                              str(actor.hunger) + ",\t" + str(actor.bathroom_need) + ",\t" +
                              actor.status + "]\n")
                else:
                    string = (string + "[" + actor.name + ",\t" + str(actor.age) + ",\t" +
                              str(actor.hunger) + ",\t" + str(actor.bathroom_need) + ",\t" +
                              actor.status + "]\n")

        return string
