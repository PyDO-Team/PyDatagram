import struct
from Datagram import Datagram

'''
The datagram iterator file responsible for retrieving values out of datagram's.
This code was largely ported from Panda3D's C++ implementation of Datagram's.
'''

class DatagramIterator:
	
	# Core functions surrounding datagrams
	def __init__(self, datagram, index=0):
		assert(isinstance(datagram, Datagram))

		self.datagram = datagram
		self.index = index

	def getBool(self):
		return self.getUint8() != 0

	def getInt8(self):
		assert(self.index < self.datagram.getLength())

	def getInt16(self):
		assert(self.index < self.datagram.getLength())

	def getInt32(self):
		assert(self.index < self.datagram.getLength())

	def getInt64(self):
		assert(self.index < self.datagram.getLength())

	def getString(self):
		stringLen = self.getUint16()
		
		assert(self.index < self.datagram.getLength())



	def getString32(self):
		assert(self.index < self.datagram.getLength())

	def getUint8(self):
		assert(self.index < self.datagram.getLength())

	def getUint16(self):
		assert(self.index < self.datagram.getLength())

	def getUint32(self):
		assert(self.index < self.datagram.getLength())

	def getUint64(self):
		assert(self.index < self.datagram.getLength())

	def getFloat32(self):
		assert(self.index < self.datagram.getLength())

	def getFloat64(self):
		assert(self.index < self.datagram.getLength())

	def getBeInt16(self):
		assert(self.index < self.datagram.getLength())

	def getBeInt32(self):
		assert(self.index < self.datagram.getLength())

	def getBeInt64(self):
		assert(self.index < self.datagram.getLength())

	def getBeUint16(self):
		assert(self.index < self.datagram.getLength())

	def getBeUint32(self):
		assert(self.index < self.datagram.getLength())

	def getBeUint64(self):
		assert(self.index < self.datagram.getLength())

	def getBeFloat32(self):
		assert(self.index < self.datagram.getLength())

	def getBeFloat64(self):
		assert(self.index < self.datagram.getLength())