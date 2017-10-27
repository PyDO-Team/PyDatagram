#from direct.distributed.PyDatagram import PyDatagram
#from direct.distributed.PyDatagramIterator import PyDatagramIterator
from PyDatagram import PyDatagram
from PyDatagramIterator import PyDatagramIterator

datagram = PyDatagram()
datagram.addInt8(63)
datagram.addBool(True)
datagram.addString("Test")

dgi = PyDatagramIterator(datagram)
int8 = dgi.getInt8()
boola = dgi.getBool()
stringa = dgi.getString()
print("Int: " + str(int8))
print("Bool: " + str(boola))
print("String: " + str(stringa))