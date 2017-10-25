from PyDatagram import PyDatagram

datagram = PyDatagram()
datagram.addInt8(120)
datagram.addString("Test")
print(datagram.getMessage())