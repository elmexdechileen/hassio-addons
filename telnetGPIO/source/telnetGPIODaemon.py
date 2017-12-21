
import telnetGPIO as tg
import time
import sys

if len(sys.argv) != 6:
    raise Exception("Not enough input arguments")

#msgBroker = str(sys.argv[1])
#msgBrokerPort = int(sys.argv[2])
#serviceName = str(sys.argv[3])
#gpioHost = str(sys.argv[4])

msgBroker = "192.168.1.145"
msgBrokerPort = 1883
serviceName = "telnetGPIO"
gpioHost = "192.168.1.171"

conn = tg.telnetGPIOHandler(msgBroker, msgBrokerPort, serviceName, gpioHost)
conn.initializeConn()

while(1 == 1):
    print(conn.newState)
    conn.read()
    conn.updateBinary()

    if(conn.newState != conn.oldState):
        conn.writeChange()

    time.sleep(float(sys.argv[5]))
