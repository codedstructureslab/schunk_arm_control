import os
import can
import struct
import time

# send all modules home
for i in range(2,3):
	set_home = "cansend can0 0E"+str(i)+"#01"
	os.system(set_home)
	print "set_home = " + str(set_home)
	time.sleep(10)


# reset all modules
for i in range(2,3):
	reset = "cansend can0 0E"+str(i)+"#00"
	os.system(reset)
	print "reset = " + str(reset)
	time.sleep(0.5)