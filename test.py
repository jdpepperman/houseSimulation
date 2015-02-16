from Simulation import *

class Test(Simulation):
	def __init__(self):
		Simulation.__init__(self)

	def setup(self):	
		self.home = House()
		
		kitchen = Kitchen(self.home, "Kitchen")
		cubbyRoom = Room(self.home, "Cubby Room")
		diningRoom = Room(self.home, "Dining Room")
		den = Room(self.home, "Den")
		joshuaBedroom = Room(self.home, "Joshua's Room")
		calebBedroom = Room(self.home, "Caleb's Room")
		raychelBedroom = Room(self.home, "Raychel's Room")
		sarahBedroom = Room(self.home, "Sarah's Room")
		parentBedroom = Room(self.home, "Parent's Room")
		hallway = Room(self.home, "Hallway")
		frontEntry = Room(self.home, "Front Entry")
		greyBathroom = Bathroom(self.home, "Grey Bathroom")
		greenBathroom = Bathroom(self.home, "Green Bathroom")
		playroom = Room(self.home, "Playroom")
		upstairsBathroom = Bathroom(self.home, "Upstairs Bathroom")
		parentBathroom = Bathroom(self.home, "Parent's Bathroom")
		laundryRoom = Room(self.home, "Laundry Room")
		
		kitchen.addConnections([cubbyRoom, diningRoom])
		den.addConnections([frontEntry, cubbyRoom, diningRoom])
		frontEntry.addConnections([playroom, hallway])
		hallway.addConnections([greyBathroom, sarahBedroom, joshuaBedroom, calebBedroom, greenBathroom, laundryRoom, parentBedroom])
		parentBedroom.addConnections([parentBathroom])
		playroom.addConnections([raychelBedroom, upstairsBathroom])


		joshua = Person(self.home, "Joshua", 21)
		joshua.hunger = 90
		joshua.putInRoom(parentBathroom)
		

sim = Test()
sim.run()
