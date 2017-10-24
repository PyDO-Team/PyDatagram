'''
The base datagram file responsible for low level datagram manipulation.
This code was largely ported from Panda3D's C++ implementation of Datagram's.
'''

class Datagram:
	
	# Core functions surrounding datagrams
	def __init__(self):
		self.datagram = None
		
	def reset(self):
		self.datagram = None
		
	def appendData(self, data, size):
		assert(int(size) >= 0)
		
	# General common use append functions.
	def addBool(self, bool):
		pass
	
	def addInt8(self, int):
		pass
		
	def addInt16(self, int):
		pass
		
	def addInt32(self, int):
		pass
		
	def addInt64(self, int):
		pass
		
	def addString(self, string):
		pass
		
	# Functions for appending the datagram with unsigned integers (UInts).	
	def addUint8(self, int):
		pass
		
	def addUint16(self, int):
		pass
		
	def addUint32(self, int):
		pass
		
	def addUint64(self, int):
		pass
		
	# Floats. You can achieve pretty good accuracy by multipling your int by 100 and then dividing by 100 on the other end of the wire.
	def addFloat32(self, float):
		pass
		
	def addFloat64(self, float):
		pass
		
	# Big Endian
	def addBeInt16(self, int):
		pass
		
	def addBeInt32(self, int):
		pass
		
	def addBeInt64(self, int):
		pass
		
	def addBeUint16(self, int):
		pass
		
	def addBeUint32(self, int):
		pass
		
	def addBeUint64(self, int):
		pass
		
	def addBeFloat32(self, float):
		pass
		
	def addBeFloat64(self, float):
		pass