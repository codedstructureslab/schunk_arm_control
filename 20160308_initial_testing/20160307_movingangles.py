import os
import can
import struct
import time


def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])

def reverse_hex(x):
    return "".join(map(str.__add__, x[-2::-2] ,x[-1::-2]))

def populate_motion_message(n, b):
    c = "cansend can0 0E"+str(n)+"#0B.04."+b[:2]+"."+b[2:4]+"."+b[4:6]+"."+b[6:8]
    print c
    return c

def main():
	# home all modules
	for i in range(1,2):
		print i
		set_home = "cansend can0 0E"+str(i)+"#01"
		os.system(set_home)
		print "set_home = " + str(set_home)
		time.sleep(0.5)


	# reset all modules
	for i in range(1,2):
		reset = "cansend can0 0E"+str(i)+"#00"
		os.system(reset)
		print "reset = " + str(reset)
		time.sleep(0.5)


	# set accelerations
	for i in range(1,2):
		set_accel = "cansend can0 0E"+str(i)+"#08.50.CD.CC.CC.3D"
		os.system(set_accel)
		print "set_accel = " + str(set_accel)
		time.sleep(0.5)


	
	# set velocities
	for i in range(1,2):
		set_vel = "cansend can0 0E"+str(i)+"#08.4F.00.00.20.41"
		os.system(set_vel)
		print "set_vel = " + str(set_vel)
		time.sleep(0.5)


	
	print "All modules homed, reset. Velocity and acceleration set."
	
	
	
	# to be received from Daniel's code
	angles = [	1.0,
				1.0,
				1.0,
				1.0,
				1.0,
				1.0,
				1.0]
	
	
	
	# loop to send move command to each module in turn
	i = 1
	for i in range(1,2):
		angle = angles[i-1]
		forwards_hex = float_to_hex(angle)
		print "Module " + str(i) + " angle in radians = " + str(angle) + " in hex = " + str(forwards_hex)
		backwards_hex = reverse_hex(forwards_hex)
		message_to_send = populate_motion_message(i, backwards_hex)
		os.system(message_to_send)
		print "should be moving module " + str(i)
		time.sleep(15)
		print "------------------------"


main()
		#current_position = populate_fetch_position_message(i)
		#while 

# test the code and run from here
