import re

while(True):
	userInput = raw_input("user: ")
	if userInput=='q':
		break

	else:
		userInput = re.sub("\?", "!", userInput)
		userInput = re.sub("What's your name", "I am Sirai", userInput)
		userInput = re.sub("What is your name", "I am Sirai", userInput)
		userInput = re.sub("Who are you", "I am Sirai", userInput)
		userInput = re.sub("What can you do", "I can do anything", userInput)
		userInput = re.sub("Can you", "I can", userInput)
		userInput = re.sub("You", "I", userInput)
		userInput = re.sub("Are you", "Yes, I am", userInput)
		userInput = re.sub("you", "I", userInput)
		userInput = re.sub(" me", " you", userInput)

		#  userInput = re.sub("", "", userInput)
	print "sirai: " + userInput+'\n'

