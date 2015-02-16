from Simulation import *

class SimName(Simulation):
	def __init__(self):
		Simulation.__init__(self)

	def setup(self):	
		#The House() to add to is called self.home

		#Room constructor:
		#Room(House house, String roomName)
		#Kitchen is the same as Room

		#Person constructor:
		#Person(House house, String name, Int age)
		

sim = SimName()
sim.run()
