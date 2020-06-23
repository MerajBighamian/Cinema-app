# mac address find
import uuid
print ("The formatted MAC address is : ", end="")
print (':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
for elements in range(0,2*6,2)][::-1]))
