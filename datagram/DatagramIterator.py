import struct
from Datagram import Datagram

'''
The datagram iterator file responsible for retrieving values out of datagram's.
This code was largely ported from Panda3D's C++ implementation of Datagram's.
'''

class DatagramIterator:
	
	# Core functions surrounding datagrams
	def __init__(self, datagram, index=0):
		self.datagram = datagram

		# How far through have we read through the datagram?
		self.index = index

	'''
	 * Extracts a boolean value.
 	'''
	def getBool(self):
		return self.getUint8() != 0

	'''
 	 * Extracts a signed 8-bit integer.
 	'''
	def getInt8(self):
		assert(self.index < self.datagram.getLength())

		data = self.datagram.getArray()
		tempVar = data[self.index]

		self.index += 1

		return tempVar

	'''
	 * Extracts a signed 16-bit integer.
 	'''
	def getInt16(self):
		assert(self.index < self.datagram.getLength())

		data = self.datagram.getArray()
		tempVar = data[self.index]

		self.index += 1

		return tempVar

	'''
 	 * Extracts a signed 32-bit integer.
 	'''
	def getInt32(self):
		assert(self.index < self.datagram.getLength())

		data = self.datagram.getArray()
		tempVar = data[self.index]

		self.index += 1

		return tempVar

	'''
 	 * Extracts a signed 64-bit integer.
 	'''
	def getInt64(self):
		assert(self.index < self.datagram.getLength())

		data = self.datagram.getArray()
		tempVar = data[self.index]

		self.index += 1

		return tempVar

	'''
	 * Extracts a variable-length string.
 	'''
	def getString(self):
		stringLen = self.getUint16()
		
		assert(self.index < self.datagram.getLength())

		data = self.datagram.getArray()
		tempVar = data[self.index]

		self.index += 1

		return tempVar

	'''
 	 * Extracts a variable-length string with a 32-bit length field.
 	'''
	def getString32(self):
		stringLen = self.getUint32()

		assert(self.index < self.datagram.getLength())

		data = self.datagram.getArray()
		tempVar = data[self.index]

		self.index += 1

		return tempVar

	'''
	 * Extracts an unsigned 8-bit integer.
 	'''
	def getUint8(self):
		assert(self.index < self.datagram.getLength())

		data = self.datagram.getArray()
		tempVar = data[self.index]

		self.index += 1

		return tempVar

	'''
	 * Extracts an unsigned 16-bit integer.
 	'''
	def getUint16(self):
		assert(self.index < self.datagram.getLength())

		data = self.datagram.getArray()
		tempVar = data[self.index]

		self.index += 1

		return tempVar

	'''
	 * Extracts an unsigned 32-bit integer.
	'''
	def getUint32(self):
		assert(self.index < self.datagram.getLength())

		data = self.datagram.getArray()
		tempVar = data[self.index]

		self.index += 1

		return tempVar

	'''
	 * Extracts an unsigned 64-bit integer.
	'''
	def getUint64(self):
		assert(self.index < self.datagram.getLength())

		data = self.datagram.getArray()
		tempVar = data[self.index]

		self.index += 1

		return tempVar

	'''
	 * Extracts a 32-bit single-precision floating-point number.
	'''
	def getFloat32(self):
		assert(self.index < self.datagram.getLength())

		data = self.datagram.getArray()
		tempVar = data[self.index]

		self.index += 1

		return tempVar

	'''
	 * Extracts a 64-bit floating-point number.
	'''
	def getFloat64(self):
		assert(self.index < self.datagram.getLength())

		data = self.datagram.getArray()
		tempVar = data[self.index]

		self.index += 1

		return tempVar

	'''
	 * Extracts a signed 16-bit big-endian integer.
	'''
	def getBeInt16(self):
		assert(self.index < self.datagram.getLength())

		data = self.datagram.getArray()
		tempVar = data[self.index]

		self.index += 1

		return tempVar

	'''
	 * Extracts a signed 32-bit big-endian integer.
	'''
	def getBeInt32(self):
		assert(self.index < self.datagram.getLength())

		data = self.datagram.getArray()
		tempVar = data[self.index]

		self.index += 1

		return tempVar

	'''
	 * Extracts a signed 64-bit big-endian integer.
	'''
	def getBeInt64(self):
		assert(self.index < self.datagram.getLength())

		data = self.datagram.getArray()
		tempVar = data[self.index]

		self.index += 1

		return tempVar

	'''
	 * Extracts an unsigned 16-bit big-endian integer.
	'''
	def getBeUint16(self):
		assert(self.index < self.datagram.getLength())

		data = self.datagram.getArray()
		tempVar = data[self.index]

		self.index += 1

		return tempVar

	'''
	 * Extracts an unsigned 32-bit big-endian integer.
	'''
	def getBeUint32(self):
		assert(self.index < self.datagram.getLength())

		data = self.datagram.getArray()
		tempVar = data[self.index]

		self.index += 1

		return tempVar

	'''
	 * Extracts an unsigned 64-bit big-endian integer.
	'''
	def getBeUint64(self):
		assert(self.index < self.datagram.getLength())

		data = self.datagram.getArray()
		tempVar = data[self.index]

		self.index += 1

		return tempVar

	'''
	 * Extracts a 32-bit big-endian single-precision floating-point number.
	'''
	def getBeFloat32(self):
		assert(self.index < self.datagram.getLength())

		data = self.datagram.getArray()
		tempVar = data[self.index]

		self.index += 1

		return tempVar

	'''
	 * Extracts a 64-bit big-endian floating-point number.
	'''
	def getBeFloat64(self):
		assert(self.index < self.datagram.getLength())

		data = self.datagram.getArray()
		tempVar = data[self.index]

		self.index += 1

		return tempVar