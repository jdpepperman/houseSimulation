from Simulation import *


class JonsHouseSim(Simulation):
    def __init__(self):
        Simulation.__init__(self)

    def setup(self):
        Simulation.setup(self)

        kitchen = Kitchen(self.home, "Kitchen")
        # living_room = Room(self.home, "Living Room")
        # hallway = Room(self.home, "Hallway")
        # jon_bedroom = Room(self.home, "Jon's Bedroom")
        # mel_bedroom = Room(self.home, "Mel's Room")
        # bathroom = Room(self.home, "Bathroom")

        # kitchen.addConnection(living_room, 'W')
        # living_room.addConnection(hallway, 'W')
        # hallway.addConnection(jon_bedroom, 'S')
        # hallway.addConnection(mel_bedroom, 'W')
        # mel_bedroom.addConnection(bathroom, 'W')

        jon = Person(self.home, "Jonathan", 21)
        # mel = Person(self.home, "Melody", 25)
        # jake = Person(self.home, "Jacob", 20)
        # diane = Person(self.home, "Diane", 45)
        # david = Person(self.home, "David", 50)

        # people = [jon, mel, jake, diane, david]

    # for person in people:
    #	person.hunger = 68


sim = JonsHouseSim()
sim.run()