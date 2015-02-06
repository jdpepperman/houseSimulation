from Room import *
from House import *
from Person import *

home = House()

kitchen = Room(home, "Kitchen")
livingRoom = Room(home, "Living Room")
diningRoom = Room(home, "Dining Room")

kitchen.addConnections([livingRoom, diningRoom])

joshua = Person(home, "Joshua")
emma = Person(home, "Emma")
