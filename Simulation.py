from Room import *
from House import *
from Person import *
from Kitchen import *
import cPickle as pickle
import time

class Simulation:
	def __init__(self):
		self.timeString = "12:00"
		self.minute = 0
		self.hour = 12
	
	def updateClock(self):
		self.minute = self.minute + 1
		if self.minute == 60:
			self.hour = self.hour + 1
			self.minute = 0
			if self.hour == 24:
				self.hour = 0
	
		self.timeString = ""
		if len(str(self.hour)) < 2:
			self.timeString = self.timeString + "0" + str(self.hour)
		else:
			self.timeString = self.timeString + str(self.hour)
	
		self.timeString = self.timeString + ":"
	
		if len(str(self.minute)) < 2:
			self.timeString = self.timeString + "0" + str(self.minute)
		else:
			self.timeString = self.timeString + str(self.minute)
	
	def run(self):	
		home = House()
		
		kitchen = Kitchen(home, "Kitchen")
		livingRoom = Room(home, "Living Room")
		diningRoom = Room(home, "Dining Room")
		bedroom1 = Room(home, "Josh's Room")
		bedroom2 = Room(home, "Emma's Room")
		hallway = Room(home, "Hallway")
		bathroom = Room(home, "Bathroom")
		laundryRoom = Room(home, "Laundry Room")
		
		kitchen.addConnections([livingRoom, diningRoom])
		hallway.addConnections([bedroom1, bedroom2, livingRoom, laundryRoom, bathroom])
		
		joshua = Person(home, "Joshua", 21)
		emma = Person(home, "Emma", 19)
		jackson = Person(home, "Jackson", 20)
		claire = Person(home, "Claire", 21)
		
		while(True):
			home.tick()
			output = open("/var/www/html/output.txt", "w")
			output.write("Time: " + self.timeString + "\n\n")
			self.updateClock()
			output.write(str(home))
			output.write("\n\n")
			output.write(home.toString_people())
			output.close()
			time.sleep(1)

sim = Simulation()
sim.run()
