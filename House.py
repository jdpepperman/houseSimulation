from Room import *
from Person import *
import random

class House(object):
	def __init__(self):
		self.rooms = []
		self.actors = []

	def __str__(self):
		h = ""
		for room in self.rooms:
			h = h + str(room) + "\n\n"
		return h[:-2]

	def __iter__(self):
		return iter(self.rooms)

	def placePersonInRoom(self, person):
		for room in self.rooms:
			if person in room.actorsInRoom:
				room.actorsInRoom.remove(person)
		i = random.randint(0, len(self.rooms)-1)
		self.rooms[i].addActor(person)

	def addRooms(self, rooms):
		for room in rooms:
			if room not in self.rooms:
				self.rooms.append(room)

	def tick(self):
		for actor in self.actors:
			actor.tick()

	def toString_people(self):
		s = "People in house [name, age, hunger, status]:\n"
		for a in self.actors:
			if isinstance(a, Person):
				if len(a.name) < 5:
					s = s + "[" + a.name + ",\t\t" + str(a.age) + ",\t" + str(a.hunger) + ",\t" + a.status + "]\n"
				else:
					s = s + "[" + a.name + ",\t" + str(a.age) + ",\t" + str(a.hunger) + ",\t" + a.status + "]\n"

		return s
