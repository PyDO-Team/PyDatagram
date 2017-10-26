from PyDatagram import PyDatagram

datagram = PyDatagram()
datagram.addInt8(127)
datagram.addString("Test")
print(datagram.getMessage())
print(datagram.getLength())