from PyDatagram import PyDatagram
from DatagramIterator import DatagramIterator

datagram = PyDatagram()
datagram.addInt8(127)
datagram.addString("Test")

dgi = DatagramIterator(datagram)