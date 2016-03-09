#This script sends the robot home and resets.

import os
import can
print "next test"
can_interface = 'can0'
bus = can.interface.Bus(can_interface, bustype='socketcan')

#reset and home
os.system("cansend can0 0E4#00")
os.system("cansend can0 0E4#01")

os.system("cansend can0 0E4#08.50.CD.CC.CC.3D")
print "Acceleration Set."

#set vel
os.system("cansend can0 0E4#08.4F.00.00.40.40")
print "Velocity Set."

#move to 90
os.system("cansend can0 0E4#0B.04.C3.F5.C8.3F")
print "Sent to 90 cmd sent."

#retrieve module state
os.system("cansend can0 0C4#0A27")
#message1 = bus.recv(2.0)  # Timeout in seconds.
#message2 = bus.recv(2.0)  # Timeout in seconds.
#message3 = bus.recv(2.0)  # Timeout in seconds.
#message4 = bus.recv(2.0)  # Timeout in seconds.
#print message1
#print message2
#print message3
#print message4


#if message1 is None:
 #   print('Timeout occurred, no message.')

#if message2 is None:
 #   print('Timeout occurred, no message.')


#os.system("cansend can0 0E6#01")
#os.system("cansend can0 0E5#00")
#os.system("cansend can0 0E5#01")
