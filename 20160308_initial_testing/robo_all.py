import os
import time
import can
import struct

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])
	




	f = raw_input("Please desired angle (float): ")
	f = float(f)
	a = float_to_hex(f)

	print "your hex code"
	print a

