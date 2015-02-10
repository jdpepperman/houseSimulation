from Room import *
from House import *
from Person import *
import cPickle as pickle
import time

timeString = "12:00"
minute = 0
hour = 12

def updateClock(self):
	minute = minute + 1
	if minute == 60:
		hour = hour + 1
		minute = 0
		if hour == 24:
			hour = 0

	timeString = ""
	if len(str(hour)) < 2:
		timeString = timeString + "0" + str(hour)
	else:
		timeString = timeString + str(hour)

	timeString = timeString + ":"

	if len(str(minute)) < 2:
		timeString = timeString + "0" + str(minute)
	else:
		timeString = timeString + str(minute)


home = House()

kitchen = Room(home, "Kitchen")
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
	output.write("Time: " + timeString + "\n")
	self.updateClock()
	output.write(str(home))
	output.write("\n\n")
	output.write(home.toString_people())
	output.close()
	time.sleep(1)
