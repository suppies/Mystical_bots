import string
#Functions for reading messages and pulling information from them

def getUser(m):
	message = m.split("!")
	x = message[0]
	x = x[1:]
	return x
	
def getMessage(m):
	message = m.split(":", 2)
	x = message[2]
	return x