from Simulation import *

class MyHouseSim(Simulation):
	def __init__(self):
		Simulation.__init__(self)

	def setup(self):	
		Simulation.setup(self)

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


		joshua = Person(self.home, "Joshua", 22)
                emma = Person(self.home, "Emma", 20)
		beth = Person(self.home, "Beth", 47)
		raychel = Person(self.home, "Raychel", 19)
		sarah = Person(self.home, "Sarah", 14)
		caleb = Person(self.home, "Caleb", 21)
                david = Person(self.home, "David", 52)
		#ellen = Person(self.home, "Ellen", 18)
		#kaylee = Person(self.home, "Kaylee", 19)
		#gary = Person(self.home, "Grayson", 16)
		#anna = Person(self.home, "Anna", 16)
		#brock = Person(self.home, "Brock", 16)

		people = [joshua, emma, raychel, sarah, caleb, beth, david]
		#for person in people:
		#	person.hunger = 68
		

sim = MyHouseSim()
sim.run()
