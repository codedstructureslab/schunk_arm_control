import struct

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])
	
def reverse_hex(x):
	return "".join(map(str.__add__, x[-2::-2] ,x[-1::-2]))

def populate_motion_message(n, b):
	c = "cansend can0 0E"+str(n)+"#0B.04."+b[:2]+"."+b[2:4]+"."+b[4:6]+"."+b[6:8]
	return c

var = 1
#struct = 1

while var == 1:
	
	f = raw_input("Please input float: ")
	n = raw_input("Please input module number: ")
	f = float(f)
	a = float_to_hex(f)

	print "your hex code"
	print a

	b = reverse_hex(a)

	print b

	c = populate_motion_message(1, b)

	print c

