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
                room1 = Room(home, "Room1")
                room2 = Room(home, "Room2")
                room3 = Room(home, "Room3")
                room4 = Room(home, "Room4")
                room5 = Room(home, "Room5")
                room6 = Room(home, "Room6")
                room7 = Room(home, "Room7")
                room8 = Room(home, "Room8")
                room9 = Room(home, "Room9")
                room10 = Room(home, "Room10")
                room11 = Room(home, "Room11")
                room12 = Room(home, "Room12")
                room13 = Room(home, "Room13")
		
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
		
		joshua = Person(home, "Joshua", 21)
                joshua.hunger = 100
		emma = Person(home, "Emma", 19)
                emma .hunger = 100
		jackson = Person(home, "Jackson", 20)
                jackson .hunger = 100
		claire = Person(home, "Claire", 21)
                claire .hunger = 100
		
		while(True):
			home.tick()
			output = open("/var/www/html/output.txt", "w")
			output.write("Time: " + self.timeString + "\n\n")
			self.updateClock()
			output.write(home.toString_people())
			output.write("\n\n")
			output.write(str(home))
			output.close()
			time.sleep(1)

sim = Simulation()
sim.run()
