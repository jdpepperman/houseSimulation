from Room import *
from House import *
from Person import *
import cPickle as pickle

home = House()

kitchen = Room(home, "Kitchen")
livingRoom = Room(home, "Living Room")
diningRoom = Room(home, "Dining Room")

kitchen.addConnections([livingRoom, diningRoom])

joshua = Person(home, "Joshua", 21)
emma = Person(home, "Emma", 19)

while(True):
	home.tick()
	output = open("/var/www/html/output.txt", "w")
	output.write(str(home))
	output.close()
