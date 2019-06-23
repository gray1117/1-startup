from __future__ import print_function 
from __future__ import unicode_literals
import math	

class Work(object):
	def __init__(self, n, h, b):
		self.basehours = 40
		self.morehours = 60
		self.name = n
		self.base = b
		self.hours = h
		
	def calcOvertime(self): ###to calc overtime rate###
		return self.base * 1.5

	def calcExtra(self): ####to calc overtime pay###
		if self.morehours > self.hours >= self.basehours:
			return (self.hours - self.basehours) * self.calcOvertime()
		elif self.basehours >= self.hours:
			return 0.00
		else:
			return 20 * self.calcOvertime()

	def calcEarnings(self):	 ####to calc total earnings###
		if self.basehours >= self.hours: 
			return self.hours * self.base
		elif self.morehours >= self.hours > self.basehours:
			return (self.basehours * self.base) + self.calcExtra() 
		else:
			return (self.basehours * self.base) + (20 * self.calcOvertime())
	
	def printOutput(self):
		print (self.name,"has worked",self.hours,"hours this week and earned",u"\u00A3",
		self.calcEarnings(),"including",u"\u00A3",self.calcExtra(),"overtime pay")
			
j = Work("John",42,7.25)
l = Work("Lucy",48,7.50)
s = Work("Sully",20,8.40)
c = Work("Chris",40,7.00)
w = Work("Will",65,8.50)

j.printOutput()
l.printOutput()
s.printOutput()
c.printOutput()
w.printOutput()
