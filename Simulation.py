from modules import *
import time
import json


class Simulation:
    def __init__(self):
        self.home = None
        self.time_string = "12:00"
        self.minute = 0
        self.hour = 12
        self.day = 1
        self.month = 1
        self.year = 2016
        self.tick_num = 0

    def updateClock(self):
        self.minute = self.minute + 1
        if self.minute == 60:
            self.hour = self.hour + 1
            self.minute = 0
        if self.hour == 24:
            self.day = self.day + 1
            self.hour = 0
        if self.day == self.daysInMonth(self.month) + 1:
            self.month = self.month + 1
            self.day = 1
        if self.month == 13:
            self.year = self.year + 1
            self.month = 1

        self.time_string = ""
        if len(str(self.hour)) < 2:
            self.time_string = self.time_string + "0" + str(self.hour)
        else:
            self.time_string = self.time_string + str(self.hour)

        self.time_string = self.time_string + ":"

        if len(str(self.minute)) < 2:
            self.time_string = self.time_string + "0" + str(self.minute)
        else:
            self.time_string = self.time_string + str(self.minute)

        self.time_string = self.time_string + ", "
        self.time_string = (self.time_string + str(self.month) + "/" + str(self.day) +
                            "/" + str(self.year))

    def daysInMonth(self, month):
        if month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif month in (4, 6, 9, 11):
            return 30
        else:
            if self.year % 4 == 0:
                if self.year % 100 == 0:
                    if self.year % 400 == 0:
                        return 29
                    else:
                        return 28
                else:
                    return 29
            else:
                return 28

    def setup(self):
        self.home = House()

    def run(self):
        self.setup()
        while True:
            self.home.tick()
            self.tick_num += 1
            output = open("output.txt", "w")
            output.write("Time: " + self.time_string + "\n\n")
            self.updateClock()
            output.write(self.home.toString_people())
            output.write("\n\n")
            output.write(str(self.home))
            output.close()

            with open('output.txt', 'w') as fp:
                fp.write(json.dumps(self.home.getDictionary(), indent=4, sort_keys=True))

            print(self.tick_num)

            #time.sleep(1)
