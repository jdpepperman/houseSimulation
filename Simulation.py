from modules import *
import cPickle as pickle
import time

class Simulation:
    # def __init__(self):
    #     self.outputFilePath = "/var/www/html/output.txt"
    #     self.timeString = "12:00"
    #     self.minute = 0
    #     self.hour = 12

    def __init__(self, outputFilePath="/var/www/html/output.txt"):
        self.outputFilePath = outputFilePath
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
    
    def setup(self):
        self.home = House()

    def run(self):
        self.setup()
        while(True):
            self.home.tick()
            output = open(self.outputFilePath, "w")
            output.write("Time: " + self.timeString + "\n\n")
            self.updateClock()
            output.write(self.home.toString_people())
            output.write("\n\n")
            output.write(str(self.home))
            output.close()
            time.sleep(1)

