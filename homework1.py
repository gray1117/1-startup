from __future__ import print_function 
from __future__ import unicode_literals
import math
	
class Work:
	def __init__(self, n, h, b):
		self.name = n
		self.hours = h
		self.base = b 
		
	def calcEarnings(self):
		return self.hours * self.base 

l = Work("Lucy",45,6.5)
s =	Work("Sully",20,8.4)
j = Work("John",33,7.5)
	
print(j.name,"has worked", j.hours,"hours this week and earned",u"\u00A3",float(j.calcEarnings()),"\n",
      s.name,"has worked", s.hours,"hours this week and earned",u"\u00A3",float(s.calcEarnings()),"\n",
	  l.name,"has worked", l.hours,"hours this week and earned",u"\u00A3",float(l.calcEarnings())) 
