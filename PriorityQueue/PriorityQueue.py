#Justin Sanny 
#CMSI 282
#Priority Queue with smallest number having priority.
#Homework 1
class PriorityQueue:
	import math
	def __init__(self):
		self.length = 0
		self.listQ = []

	def peek(self):
		if self.is_empty():
			raise ValueError( "Loser! It was empty! NOOOOO!")
		return self.listQ[0]

	def add(self, item):
		self.listQ.append(item)
		self.length += 1
		templength = self.length
		if templength == 1:
			pass
		else:
			while self.listQ[math.floor((templength - 1) / 2) ] > item or self.listQ[math.floor((templength - 2) / 2)] > item:
				if templength == 1:
					break
				elif templength % 2 == 0 and self.listQ[math.floor((templength - 1) / 2) ] > item:
					self.listQ[templength - 1] = self.listQ[math.floor((templength - 1) / 2)]
					self.listQ[math.floor((templength - 1) / 2)] = item
					templength = math.floor((templength) / 2)
				elif templength % 2 == 1 and self.listQ[math.floor((templength - 2) / 2)] > item:
					self.listQ[templength - 1] = self.listQ[math.floor((templength - 2) / 2)]
					self.listQ[math.floor((templength - 2) / 2)] = item
					templength = math.floor((templength - 1) / 2)
				else:
					break
	def remove(self):
		n = 0
		if self.is_empty():
			raise ValueError( "Nope, nothing's there!")
		firstitem = self.peek()
		self.listQ[0] = self.listQ[self.length - 1] 
		item = self.peek()
		self.listQ.pop()
		self.length -= 1
		while n < self.length - 1:
			if (2 * n + 1) > self.length - 1:
				break
			elif (2 * n + 2) > self.length - 1 and 2 * n + 1 == self.length:
				self.listQ[n] = self.listQ[2 * n + 1]
				self.listQ[2 * n + 1] = item
				break
			elif (2 * n + 2) > self.length - 1:
				self.listQ[n] = self.listQ[2 * n + 1]
				self.listQ[2 * n + 1] = item
				n = 2* n + 1
			elif self.listQ[2 * n + 2] > self.listQ[2 * n + 1]:
				self.listQ[n] = self.listQ[2 * n + 1]
				self.listQ[2 * n + 1] = item
				n = 2 * n + 1
			elif self.listQ[2 * n + 2] < self.listQ[2 * n + 1]:
				self.listQ[n] = self.listQ[2 * n + 2]
				self.listQ[2 * n + 2] = item
				n = 2 * n + 2
			else: 
				break
		return firstitem
	def __len__(self):
		return str(self.length)

	def is_empty(self):
		return self.length == 0

	def __str__(self):
		n = 0
		result = "["
		while self.length > n:
			result += str(self.listQ[n]) + ','
			n += 1
		result += "]"
		return result
