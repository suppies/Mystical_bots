import socket
from Settings import HOST,PORT, PASS, NAME, CHANNEL

#irc protocol stuff, creats a socket that is connected to server specified in settings
def openSocket():
	s = socket.socket()
	s.connect((HOST,PORT))
	message = "PASS " + PASS + "\r\n"
	s.sendto(message.encode('utf-8'),(HOST,PORT))
	message = "NICK " + NAME + "\r\n"
	s.sendto(message.encode('utf-8'),(HOST,PORT))
	message = "JOIN #" + CHANNEL + "\r\n"
	s.sendto(message.encode('utf-8'),(HOST,PORT))
	return s

#allows the bot to send message to the socket
def sendMessage(s, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	s.send(bytes(messageTemp + "\r\n" , "UTF-8"))
	print("Sent: " +messageTemp)