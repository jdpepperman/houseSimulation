import random
from Actor import Actor
from Room import Room


class Person(Actor):
    def __init__(self, house, name, age):
        Actor.__init__(self, house, name)
        self.house.placePersonInRoom(self)
        self.age = age
        self.going_to_room = None
        self.minute_count = 0
        self.hunger = random.randint(0, 20)
        self.bathroom_need = random.randint(0, 10)
        self.travel_room = []

        self.print_flag = False

    def __str__(self):
        string = "Name: " + self.name + "\n"
        string = string + "Age: " + str(self.age) + "\n"
        string = string + "\n"

        return string

    def getDictionary(self):
        return_dict = {
            'name': self.name,
            'age': self.age,
            'hunger': self.hunger,
            'bathroom_need': self.bathroom_need
        }
        return return_dict

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
        return (self.hunger >= random.randint(75, 100) or self.hunger > 100 or
                self.status == "eating" or self.status == "moving to Kitchen")

    def __bathroom(self):
        # self.print_flag = True
        return (self.bathroom_need >= random.randint(75, 100) or self.bathroom_need > 100 or
                self.status == "pooping" or self.status == "moving to Bathroom")

    def wander(self):
        """Makes the person randomly pick a room that he can go to (including the one he's in)
           and go there"""
        self.status = "wandering"
        possible_rooms_to_go_to = []
        possible_rooms_to_go_to.append(self.getRoom())
        possible_rooms_to_go_to.extend(self.getRoom().getConnections())

        room_to_go_to = possible_rooms_to_go_to[random.randint(0, len(possible_rooms_to_go_to) - 1)]
        self.moveToRoom(room_to_go_to)

    def moveTowardRoomType(self, roomType):
        """Makes the person move in the direction of a room of type roomType.
           If one is not present in the house, he will wander instead."""
        # if we're looking for a specific Room
        if isinstance(roomType, Room):
            if roomType in self.house.getRooms():
                self.status = "moving to " + type(roomType).__name__
                current_room = self.getRoom()
                # traverse the graph and look for a path. then move along it
                self.fprint(self.name + " is " +
                            "In room: " + current_room.name)
                room_to_go_to = self.__getRoomTowardRoomType(roomType)
                self.moveToRoom(roomType)
            else:
                self.wander()
        # if we're looking for a room type
        else:
            if self.house.hasRoomType(roomType):
                self.status = "moving to " + roomType.__name__
                current_room = self.getRoom()
                # traverse the graph and look for a path. then move along it
                self.fprint(self.name + " is " +
                            "In room: " + current_room.name)
                room_to_go_to = self.__getRoomTowardRoomType(roomType)
                self.moveToRoom(room_to_go_to)
            else:
                self.wander()

    def __getRoomTowardRoomType(self, roomType):
        # if we're looking for a specific Room
        if isinstance(roomType, Room):
            self.connected = False

            def isConnected(r, rt):
                to_check = r.getConnections()
                room_checked_status[r] = True
                self.fprint(self.name + " is " + "\tIs " +
                            r.name + " connected to " + rt.name + "?")
                for room in to_check:
                    self.fprint(self.name + " is " + "\t\tChecking " + room.name)
                    if room_checked_status[room] is False:
                        if room == rt:
                            self.fprint(self.name + " is " + "True")
                            self.connected = True
                        else:
                            isConnected(room, rt)
                return self.connected

            # set up the checked status of each room in the house
            room_checked_status = {}
            for room in self.house.getRooms():
                room_checked_status[room] = False

            from_room = self.getRoom()
            room_checked_status[from_room] = True
            for room in from_room.getConnections():
                room_checked_status[room] = True
                if room == roomType:
                    if room.can_enter:
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
                to_check = r.getConnections()
                room_checked_status[r] = True
                self.fprint(self.name + " is " + "\tIs " + r.name +
                            " connected to " + rt.__name__ + "?")
                for room in to_check:
                    self.fprint(self.name + " is " + "\t\tChecking " + room.name)
                    if room_checked_status[room] is False:
                        if isinstance(room, rt):
                            self.fprint(self.name + " is " + "True")
                            # make this the room we go to no matter what now
                            self.going_to_room = room
                            self.connected = True
                        else:
                            isConnected(room, rt)
                return self.connected

            # set up the checked status of each room in the house
            room_checked_status = {}
            for room in self.house.getRooms():
                room_checked_status[room] = False

            from_room = self.getRoom()
            room_checked_status[from_room] = True
            for room in from_room.getConnections():
                room_checked_status[room] = True
                if isinstance(room, roomType) or isConnected(room, roomType):
                    return room

    def eat(self):
        from modules.Kitchen import Kitchen
        if isinstance(self.getRoom(), Kitchen):
            self.status = "eating"
            self.hunger = self.hunger - random.randint(1, 4)
            if self.hunger < random.randint(0, 20):
                self.status = "idle"
        else:
            if self.going_to_room is None:
                self.moveTowardRoomType(Kitchen)
            else:
                self.moveTowardRoomType(self.going_to_room)

    def poop(self):
        from modules.Bathroom import Bathroom
        if isinstance(self.getRoom(), Bathroom):
            self.status = "pooping"
            self.bathroom_need = self.bathroom_need - random.randint(7, 14)
            if self.bathroom_need < random.randint(0, 7):
                self.status = "idle"
        else:
            if self.going_to_room is None:
                self.moveTowardRoomType(Bathroom)
            else:
                self.moveTowardRoomType(self.going_to_room)

    def calcAge(self):
        self.minute_count = self.minute_count + 1
        if self.minute_count >= 525949:
            self.age = self.age + 1
            self.minute_count = 0

    def setAge(self, age):
        self.age = age

    def alterStats(self):
        if self.status == "idle":
            self.going_to_room = None

        inc_hunger = random.randint(0, 100)
        if inc_hunger < 25:
            self.hunger = self.hunger + 1

        inc_bathroom = random.randint(0, 100)
        # use this to subtract something to do with how hungry they are
        # ...somehow they need to have to go more if they've eaten recently
        inc_bathroom = inc_bathroom - 0
        if inc_hunger < 25:
            self.bathroom_need = self.bathroom_need + 1

    def fprint(self, string):
        if self.print_flag:
            print string
