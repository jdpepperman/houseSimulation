from Simulation import *


class MyHouseSim(Simulation):
    def __init__(self):
        Simulation.__init__(self)

    def setup(self):
        Simulation.setup(self)

        kitchen = Kitchen(self.home, "Kitchen")
        livingRoom = Room(self.home, "Living Room")
        hallway = Room(self.home, "Hallway")
        jonBedroom = Room(self.home, "Jon's Bedroom")
        melBedroom = Room(self.home, "Mel's Room")
        bathroom = Room(self.home, "Bathroom")

        kitchen.addConnection(livingRoom, 'W')
        livingRoom.addConnection(hallway, 'W')
        hallway.addConnection(jonBedroom, 'S')
        hallway.addConnection(melBedroom, 'W')
        melBedroom.addConnection(bathroom, 'W')

        jon = Person(self.home, "Jonathan", 21)
        mel = Person(self.home, "Melody", 25)
        jake = Person(self.home, "Jacob", 20)
        diane = Person(self.home, "Diane", 45)
        david = Person(self.home, "David", 50)

        people = [jon, mel, jake, diane, david]

    # for person in people:
    #	person.hunger = 68


sim = MyHouseSim()
sim.run()
