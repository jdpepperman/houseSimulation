from Simulation import *


class FindKitchenSim(Simulation):
    def __init__(self):
        Simulation.__init__(self)

    def setup(self):
        self.home = House()

        kitchen = Kitchen(self.home, "Kitchen")
        room1 = Room(self.home, "Room1")
        room2 = Room(self.home, "Room2")
        room3 = Room(self.home, "Room3")
        room4 = Room(self.home, "Room4")
        room5 = Room(self.home, "Room5")
        room6 = Room(self.home, "Room6")
        room7 = Room(self.home, "Room7")
        room8 = Room(self.home, "Room8")
        room9 = Room(self.home, "Room9")
        room10 = Room(self.home, "Room10")
        room11 = Room(self.home, "Room11")
        room12 = Room(self.home, "Room12")
        room13 = Room(self.home, "Room13")

        kitchen.addConnections([room1])
        room1.addConnections([room2])
        room2.addConnections([room3])
        room3.addConnections([room4])
        room4.addConnections([room5])
        room5.addConnections([room6])
        room6.addConnections([room7])
        room7.addConnections([room8])
        room8.addConnections([room9])
        room9.addConnections([room10])
        room10.addConnections([room11])
        room11.addConnections([room12])
        room12.addConnections([room13])

        joshua = Person(self.home, "Joshua", 21)
        joshua.hunger = 100
        joshua.putInRoom(room13)

        # emma = Person(self.home, "Emma", 19)
        # emma .hunger = 100
        # jackson = Person(self.home, "Jackson", 20)
        # jackson .hunger = 100
        # claire = Person(self.home, "Claire", 21)
        # claire .hunger = 100

        # people = [joshua, emma, claire, jackson]
        # for p in people:

        # p.putInRoom(room13)


sim = FindKitchenSim()
sim.run()
