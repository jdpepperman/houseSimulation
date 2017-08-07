from modules import *
import time


class Simulation:
    def __init__(self):
        self.timeString = "12:00"
        self.minute = 0
        self.hour = 12
        self.day = 1
        self.month = 1
        self.year = 2016
        self.tickNum = 0

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

        self.timeString = self.timeString + ", "
        self.timeString = self.timeString + str(self.month) + "/" + str(self.day) + "/" + str(self.year)

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
        while (True):
            self.home.tick()
            self.tickNum += 1
            output = open("output.txt", "w")
            output.write("Time: " + self.timeString + "\n\n")
            self.updateClock()
            output.write(self.home.toString_people())
            output.write("\n\n")
            output.write(str(self.home))
            output.close()
            print(self.tickNum)
        # time.sleep(1)
