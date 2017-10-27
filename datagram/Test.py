from direct.distributed.PyDatagram import PyDatagram
#from PyDatagram import PyDatagram
from DatagramIterator import DatagramIterator

datagram = PyDatagram()
datagram.addInt8(63)
datagram.addBool(True)
datagram.addString("Test")

dgi = DatagramIterator(datagram)
int8 = dgi.getInt8()
boola = dgi.getBool()
stringa = dgi.getString()
print("Int: " + str(int8))
print("Bool: " + str(boola))
print("String: " + str(stringa))