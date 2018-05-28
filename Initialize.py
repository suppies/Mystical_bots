import string
from Socket import sendMessage
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
			
def loadingComplete(line):
	if("End of /NAMES list" in line):
		return False
	else:
		return True