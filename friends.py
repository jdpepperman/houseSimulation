from Simulation import *

class Friends(Simulation):
	def __init__(self):
		Simulation.__init__(self)
	
	def setup(self):	
		self.home = House()
		
		kitchen = Kitchen(self.home, "Kitchen")
		livingRoom = Room(self.home, "Living Room")
		diningRoom = Room(self.home, "Dining Room")
		joshuaBedroom = Room(self.home, "Joshua's Room")
		emmaBedroom = Room(self.home, "Emma's Room")
		jacksonBedroom = Room(self.home, "Jackson's Room")
		claireBedroom = Room(self.home, "Claire's Room")
		hallway = Room(self.home, "Hallway")
		bathroom = Bathroom(self.home, "Bathroom")
		laundryRoom = Room(self.home, "Laundry Room")
		
		kitchen.addConnections([livingRoom, diningRoom])
		hallway.addConnections([joshuaBedroom, emmaBedroom, claireBedroom, jacksonBedroom, livingRoom, laundryRoom, bathroom])
		#kitchen.addConnections([bathroom])
		#hallway.addConnections([livingRoom, bathroom])
		
		joshua = Person(self.home, "Joshua", 21)
		joshua.hunger = 69
		emma = Person(self.home, "Emma", 19)
		jackson = Person(self.home, "Jackson", 20)
		claire = Person(self.home, "Claire", 21)
		

sim = Friends()
sim.run()
