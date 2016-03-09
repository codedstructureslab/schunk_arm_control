import struct

def hex_to_float(f):
	return struct.unpack('!f', f.decode('hex'))[0]

var = 1
#struct = 1

while var == 1:
	
	f = raw_input("Please input hex: ")
	n = raw_input("Please input module number: ")
	a = hex_to_float(f)

	print "your float"
	print a
