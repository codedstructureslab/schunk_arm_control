#linuxversion.py

#Have user input version and print response

import os
import time
import can

#can_interface = 'can0'
#bus = can.interface.Bus(can_interface, bustype='socketcan_native')
#message = bus.recv()
print "Hello. My name is Robo Man!"

print "I am going home."

#reset and home



os.system("cansend can0 0E6#01")
#os.system("cansend can0 0E5#00")
#os.system("cansend can0 0E5#01")
time.sleep(5)
os.system("cansend can0 0E6#00")

#set accel
os.system("cansend can0 0E6#08.50.CD.CC.CC.3D")
#os.system("cansend can0 0E5#08.50.CD.CC.CC.3D")
print "Acceleration Set."

#set vel
os.system("cansend can0 0E6#08.4F.00.00.40.40")
#os.system("cansend can0 0E5#08.4F.00.00.40.40")
print "Velocity Set."
os
#move to 90
os.system("cansend can0 0E6#0B.04.C3.F5.C8.3F")
#os.system("cansend can0 0E5#0B.04.C3.F5.C8.3F")
print "Sent to 90 cmd sent."
time.sleep(15)


#move to -90
#os.system("cansend can0 0E6#0B.04.C3.F5.C8.BF")
#os.system("cansend can0 0E5#0B.04.C3.F5.C8.BF")
#print "Sent to -90 cmd sent."
#time.sleep(15)

#halt
#os.system("cansend can0 0E6#02")

print "Good bye."

#name = raw_input("What Linux release do you use?")

#print "I also like", name, " - Linux rules!"
