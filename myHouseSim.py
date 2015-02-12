from modules import *
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
		cubbyRoom = Room(home, "Cubby Room")
		diningRoom = Room(home, "Dining Room")
		den = Room(home, "Den")
		joshuaBedroom = Room(home, "Joshua's Room")
		calebBedroom = Room(home, "Caleb's Room")
		raychelBedroom = Room(home, "Raychel's Room")
		sarahBedroom = Room(home, "Sarah's Room")
		parentBedroom = Room(home, "Parent's Room")
		hallway = Room(home, "Hallway")
		frontEntry = Room(home, "Front Entry")
		greyBathroom = Bathroom(home, "Grey Bathroom")
		greenBathroom = Bathroom(home, "Green Bathroom")
		playroom = Room(home, "Playroom")
		upstairsBathroom = Bathroom(home, "Upstairs Bathroom")
		parentBathroom = Bathroom(home, "Parent's Bathroom")
		laundryRoom = Room(home, "Laundry Room")
		
		kitchen.addConnections([cubbyRoom, diningRoom])
		den.addConnections([frontEntry, cubbyRoom, diningRoom])
		frontEntry.addConnections([playroom, hallway])
		hallway.addConnections([greyBathroom, sarahBedroom, joshuaBedroom, calebBedroom, greenBathroom, laundryRoom, parentBedroom])
		parentBedroom.addConnections([parentBathroom])
		playroom.addConnections([raychelBedroom, upstairsBathroom])


		joshua = Person(home, "Joshua", 21)
		emma = Person(home, "Emma", 19)
		raychel = Person(home, "Raychel", 18)
		sarah = Person(home, "Sarah", 13)
		caleb = Person(home, "Caleb", 19)
		ellen = Person(home, "Ellen", 18)
		kaylee = Person(home, "Kaylee", 19)
		gary = Person(home, "Grayson", 16)
		anna = Person(home, "Anna", 16)
		brock = Person(home, "Brock", 16)
		
		while(True):
			home.tick()
			output = open("/var/www/html/output.txt", "w")
			output.write("Time: " + self.timeString + "\n\n")
			output.write(home.toString_people())
			output.write("\n\n")
			self.updateClock()
			output.write(str(home))
			output.close()
			time.sleep(1)

sim = Simulation()
sim.run()
