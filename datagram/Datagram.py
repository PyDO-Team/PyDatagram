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

	'''
 	 * Returns the datagram's data as a string.
 	'''
	def getMessage(self):
		return ''.join(self._data)

	'''
 	 * Returns the number of bytes in the datagram.
 	'''
	def getLength(self):
		return len(self.getMessage())
	
	'''
 	 * Returns the actual array used in the Datagram.
 	 * We use a list over an array, but you get the point.
 	 * Generally this should never be called.
 	'''
	def getArray(self):
		return self._data
		
	# General common use append functions.

	'''
 	 * Adds a boolean value to the datagram.
 	'''
	def addBool(self, bool):
		# Check if the parsed value is actually a bool.
		assert(int(bool) == 0 or int(bool) == 1)
		self.addUint8(int(bool))
	
	'''
 	 * Adds a signed 8-bit integer to the datagram.
 	'''
	def addInt8(self, int):
		# Check if the parsed value is an Int8.
		assert(int >= -128 and int <= 127)
		data = struct.pack('<i', int)
		self.appendData(data, len(str(int)))
		
	'''
 	 * Adds a signed 16-bit integer to the datagram.
 	'''
	def addInt16(self, int):
		# Check if the parsed value is an Int16.
		assert(int >= -32768 and int <= 32767)
		data = struct.pack('<i', int)
		self.appendData(data, len(str(int)))
		
	'''
 	 * Adds a signed 32-bit integer to the datagram.
 	'''
	def addInt32(self, int):
		# Check if the parsed value is an Int32.
		assert(int >= -2147483648 and int <= 2147483647)
		data = struct.pack('<i', int)
		self.appendData(data, len(str(int)))

	'''
 	 * Adds a signed 64-bit integer to the datagram.
 	'''	
	def addInt64(self, int):
		# Check if the parsed value is an Int64.
		assert(int >= -9223372036854775808 and int <= 9223372036854775807)
		data = struct.pack('<i', int)
		self.appendData(data, len(str(int)))

	'''
 	 * Adds a variable-length string to the datagram. This actually adds a count
 	 * followed by n bytes.
 	'''
	def addString(self, string):
		# The max sendable length for a normal string is 2^16.
		# Check if the string is less than or equal to the max length.
		assert(len(string) <= 65535)

		# Strings always are preceded by their length.
		self.addUint16(len(string))
		self.appendData(string, len(string))

	'''
 	 * Adds a variable-length string to the datagram, using a 32-bit length field
 	 * to allow very long strings.
 	'''
 	def addString32(self, string):
		# Strings always are preceded by their length.
		self.addUint32(len(string))
		self.appendData(string, len(string))
		
	# Functions for appending the datagram with unsigned integers (UInts).

	'''
 	 * Adds an unsigned 8-bit integer to the datagram.
 	'''
	def addUint8(self, int):
		# Check if the parsed value is an Unsigned Int8.
		assert(int >= 0 and int <= 255)
		data = struct.pack('<I', int)
		self.appendData(data, len(str(int)))
	
	'''
 	 * Adds an unsigned 16-bit integer to the datagram.
 	'''
	def addUint16(self, int):
		# Check if the parsed value is an Unsigned Int16.
		assert(int >= 0 and int <= 65535)
		data = struct.pack('<I', int)
		self.appendData(data, len(str(int)))

	'''
 	 * Adds an unsigned 32-bit integer to the datagram.
 	'''
	def addUint32(self, int):
		# Check if the parsed value is an Unsigned Int32.
		assert(int >= 0 and int <= 4294967295)
		data = struct.pack('<I', int)
		self.appendData(data, len(str(int)))

	'''
	 * Adds an unsigned 64-bit integer to the datagram.
 	'''
	def addUint64(self, int):
		# Check if the parsed value is an Unsigned Int64.
		assert(int >= 0 and int <= 18446744073709551615)
		data = struct.pack('<I', int)
		self.appendData(data, len(str(int)))
		
	# Functions for appending the datagram with floats.

	'''
 	 * Adds a 32-bit single-precision floating-point number to the datagram.
 	 * Since this kind of float is not necessarily portable across different
 	 * architectures, special care is required.
 	'''
	def addFloat32(self, float):
		data = struct.pack('<f', float)
		self.appendData(data, len(str(float)))
		
	'''
 	 * Adds a 64-bit floating-point number to the datagram.
 	'''
	def addFloat64(self, float):
		data = struct.pack('<f', float)
		self.appendData(data, len(str(float)))
		
	# Big Endian formated functions.

	'''
 	 * Adds a signed 16-bit big-endian integer to the datagram.
 	'''
	def addBeInt16(self, int):
		# Check if the parsed value is an Int16.
		assert(int >= -32768 and int <= 32767)
		data = struct.pack('>i', int)
		self.appendData(data, len(str(int)))
		
	'''
 	 * Adds a signed 32-bit big-endian integer to the datagram.
 	'''
	def addBeInt32(self, int):
		# Check if the parsed value is an Int32.
		assert(int >= -2147483648 and int <= 2147483647)
		data = struct.pack('>i', int)
		self.appendData(data, len(str(int)))
		
	'''
 	 * Adds a signed 64-bit big-endian integer to the datagram.
 	'''
	def addBeInt64(self, int):
		# Check if the parsed value is an Int64.
		assert(int >= -9223372036854775808 and int <= 9223372036854775807)
		data = struct.pack('>i', int)
		self.appendData(data, len(str(int)))
		
	'''
	 * Adds an unsigned 16-bit big-endian integer to the datagram.
 	'''
	def addBeUint16(self, int):
		# Check if the parsed value is an Unsigned Int16.
		assert(int >= 0 and int <= 65535)
		data = struct.pack('>I', int)
		self.appendData(data, len(str(int)))
		
	'''
 	 * Adds an unsigned 32-bit big-endian integer to the datagram.
 	'''	
	def addBeUint32(self, int):
		# Check if the parsed value is an Unsigned Int32.
		assert(int >= 0 and int <= 4294967295)
		data = struct.pack('>I', int)
		self.appendData(data, len(str(int)))
		
	'''
 	 * Adds an unsigned 64-bit big-endian integer to the datagram.
 	'''
	def addBeUint64(self, int):
		# Check if the parsed value is an Unsigned Int64.
		assert(int >= 0 and int <= 18446744073709551615)
		data = struct.pack('>I', int)
		self.appendData(data, len(str(int)))

	'''
 	 * Adds a 32-bit single-precision big-endian floating-point number to the
 	 * datagram.
 	'''
	def addBeFloat32(self, float):
		data = struct.pack('>f', float)
		self.appendData(data, len(str(float)))
		
	'''
 	 * Adds a 64-bit big-endian floating-point number to the datagram.
 	'''	
	def addBeFloat64(self, float):
		data = struct.pack('>f', float)
		self.appendData(data, len(str(float)))