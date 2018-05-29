import string
from Socket import sendMessage
#shows when a socket has connected to a server, does not connect bot to server.  Clears the buffer

#joinRoom prints messages form server while bot is connecting to the server
def joinRoom(s):
	buffer = ""
	Loading = True
	while Loading:
		buffer = buffer + s.recv(2048).decode("utf-8")
		temp = buffer.split("\n")
		buffer = temp.pop()
		
		for line in temp:
			print(line)
			Loading = loadingComplete(line)
	sendMessage(s, "Joined chat")

#helper function for loadingComplete, does check for last line before connecting		
def loadingComplete(line):
	if("End of /NAMES list" in line):
		return False
	else:
		return True