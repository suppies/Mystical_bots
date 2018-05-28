from Socket import openSocket, sendMessage
from Initialize import joinRoom
import string

s = openSocket()
joinRoom(s)

while True:
	
	buffer = s.recv(2048).decode("utf-8")
	temp = buffer.split("\n")
	buffer = temp.pop()
	
	for line in temp:
		print(line)
		sendMessage(s, "Greetings my dude")
        
