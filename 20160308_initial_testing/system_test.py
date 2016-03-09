os.system("cansend can0 100#08.4F.00.00.40.40")
import os
import can
import struct


def float_to_hex(f):
   return hex(struct.unpack('<I', struct.pack('<f', f))[0])

def reverse_hex(x):
   return "".join(map(str.__add__, x[-2::-2] ,x[-1::-2]))

def populate_motion_message(n, b):
   c = "cansend can0 0E"+n+"#0B.04."+b[:2]+"."+b[2:4]+"."+b[4:6]+"."+b[6:8]
   return c

def main():
# home all modules
os.system("cansend can0 100#01")

# reset all modules
os.system("cansend can0 100#00")

# set velocities
os.system("cansend can0 100#08.4F.00.00.40.40")

# set accelerations
os.system("cansend can0 100#08.50.CD.CC.CC.3D")

print "All modules homed, reset. Velocity and acceleration set."



# to be received from Daniel's code
angles = [ 0.5,
0.5,
0,
0.5,
0.5,
0.5,
0.5]



# loop to send move command to each module in turn
i = 1
for i in range(len(angles)+1):
angle = angle[i-1]
forwards_hex = float_to_hex(angle)
print "Module " + str(i) + " angle in radians = " + str(angle) + " in hex = " + str(forwards_hex)
backwards_hex = reverse_hex(forwards_hex)
message_to_send = populate_motion_message(i, backwards_hex)
os.system(message_to_send)
time.sleep(15)


main()
#current_position = populate_fetch_position_message(i)
#while

# test the code and run from here
