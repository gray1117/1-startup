from __future__ import print_function 
from __future__ import unicode_literals
import math	

class Work:
	def __init__(self, n, h, b, o):
		self.basehours = 40
		self.morehours = 60
		self.name = n
		self.base = b
		self.hours = h
		self.overtime = o

	def calcExtra(self): ####this is to calc overtime pay###
		if self.morehours > self.hours >= self.basehours:
			return (self.hours - self.basehours) * self.overtime
		elif self.basehours >= self.hours:
			return 0.00
		else:
			return 20 * self.overtime

	def calcEarnings(self):	 ####this is to calc total earnings###
		if self.basehours >= self.hours: 
			return self.hours * self.base
		elif self.morehours >= self.hours > self.basehours:
			return (self.basehours * self.base) + self.calcExtra() 
		else:
			return (self.basehours * self.base) + (20 * self.overtime)
	
j = Work("John",42,7.25,10.86)
s = Work("Sully",20,8.40,12.60)
c = Work("Chris",40,7.00,10.50)
w = Work("Will",65,8.50,12.75)

print(j.name,"has worked", j.hours,"hours this week and earned",u"\u00A3",j.calcEarnings(),"including",u"\u00A3",j.calcExtra(),"overtime pay")
print(s.name,"has worked", s.hours,"hours this week and earned",u"\u00A3",s.calcEarnings(),"including",u"\u00A3",s.calcExtra(),"overtime pay")
print(c.name,"has worked", c.hours,"hours this week and earned",u"\u00A3",c.calcEarnings(),"including",u"\u00A3",c.calcExtra(),"overtime pay")
print(w.name,"has worked", w.hours,"hours this week and earned",u"\u00A3",w.calcEarnings(),"including",u"\u00A3",w.calcExtra(),"overtime pay")
