import struct

'''
The base datagram file responsible for low level datagram manipulation.
This code was largely ported from Panda3D's C++ implementation of Datagram's.
'''

class Datagram:
	
	# Core functions surrounding datagrams
	def __init__(self):
		self._data = []
		
	def reset(self):
		self._data = []

	# The next two functions are a fancy way of building/appending our datagram
	# which is much faster than just adding two string's together.
	def appendData(self, data, size):
		assert(int(size) >= 0)

		self._data.append(data)

	def getMessage(self):
		return ''.join(self._data)
		
	# General common use append functions.
	def addBool(self, bool):
		self.addUint8(int(bool))
	
	def addInt8(self, int):
		data = struct.pack('<i', int)
		self.appendData(data, 1)
		
	def addInt16(self, int):
		# TODO - Little Endianness
		self.appendData(int, len(int))
		
	def addInt32(self, int):
		# TODO - Little Endianness
		self.appendData(int, len(int))
		
	def addInt64(self, int):
		# TODO - Little Endianness
		self.appendData(int, len(int))
		
	def addString(self, string):
		# The max sendable length for a string is 2^16.
		# Check if the string is less than or equal to the max length.
		assert(len(string) <= 65536)

		# Strings always are preceded by their length.
		self.addUint16(len(string))

		self.appendData(string, len(string))
		
	# Functions for appending the datagram with unsigned integers (UInts).	
	def addUint8(self, int):
		self.appendData(int, 1)
		
	def addUint16(self, int):
		data = struct.pack('<I', int)
		self.appendData(data, len(str(int)))

	def addUint32(self, int):
		# TODO - Little Endianness
		self.appendData(int, len(int))
		
	def addUint64(self, int):
		# TODO - Little Endianness
		self.appendData(int, len(int))
		
	# Floats. You can achieve pretty good accuracy by multipling your int by 100 and then dividing by 100 on the other end of the wire.
	def addFloat32(self, float):
		# TODO - Little Endianness
		self.appendData(float, len(float))
		
	def addFloat64(self, float):
		# TODO - Little Endianness
		self.appendData(float, len(float))
		
	# Big Endian
	def addBeInt16(self, int):
		# TODO - Big Endianness
		self.appendData(int, len(int))
		
	def addBeInt32(self, int):
		# TODO - Big Endianness
		self.appendData(int, len(int))
		
	def addBeInt64(self, int):
		# TODO - Big Endianness
		self.appendData(int, len(int))
		
	def addBeUint16(self, int):
		# TODO - Big Endianness
		self.appendData(int, len(int))
		
	def addBeUint32(self, int):
		# TODO - Big Endianness
		self.appendData(int, len(int))
		
	def addBeUint64(self, int):
		# TODO - Big Endianness
		self.appendData(int, len(int))
		
	def addBeFloat32(self, float):
		# TODO - Big Endianness
		self.appendData(float, len(float))
		
	def addBeFloat64(self, float):
		# TODO - Big Endianness
		self.appendData(float, len(float))