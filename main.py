import Queue
import time
from cpconsole import CpConsole
from cpmodem import CpModem
from cpcomm import CpComm

from datetime import datetime


def modemDataReceived(data):
    print data
    
def rfDataReceived(data):
    print data
    
def inetDataReceived(data):
    print data

if __name__ == '__main__':

    print "Init complete: ready for serial communication!"

    modemThread = CpModem(modemDataReceived)
    modemThread.start()
    
    commThread = CpComm(modemThread)
    commThread.start()
    
    consoleThread = CpConsole(modemThread, commThread)
    consoleThread.start()
    
    while(consoleThread.isAlive()):
        time.sleep(.005)

    print 'Exiting App...'
    print 'Exiting App...'
    exit()
    
    


