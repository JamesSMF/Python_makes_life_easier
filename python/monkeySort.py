import random

def is_sorted(theList):
	for i in range(1, len(theList)):
		if theList[i] < theList[i-1]:
			return False
	return True
# end def

s = raw_input("Please enter the numbers, splited by space: \n")
data = map(int, s.split())

while not is_sorted(data):
	random.shuffle(data)
# end while

print data
