from Socket import openSocket, sendMessage
from Initialize import joinRoom
from ReadChat import getUser, getMessage
import string
#Runs the Bot

f = open("BadWords.txt")
words = f.readlines()

s = openSocket()
joinRoom(s)

while True:
	
	buffer = s.recv(2048).decode("utf-8")
	temp = buffer.split("\n")
	buffer = temp.pop()
	
	for line in temp:
		message = getMessage(line)
		user = getUser(line)
		print(user + ":" + message)
		for word in words:
			word = word[:-1]
			if word in message:
				sendMessage(s, "/timeout " + user + " 1")