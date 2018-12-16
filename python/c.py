from collections import OrderedDict
from datetime import datetime
from itertools import imap
import re

# This fuction prints out date and time in a clear formate.
# This function takes a string input, and returns a string.
def dateFormat(dateStr):
	dateList = []          # declare an empty list
	for i in range(4):     # stores year
		dateList.append(dateStr[i])
	dateList.append('-')
	for i in range(4, 6):  # stores month
		dateList.append(dateStr[i])
	dateList.append('-')
	for i in range(6, 8):  # stores day
		dateList.append(dateStr[i])
	dateList.append('  ')
	for i in range(8, 10): # stores hour
		dateList.append(dateStr[i])
	dateList.append(' : ') # stores minute
	for i in range(10, 12):
		dateList.append(dateStr[i])

	returnStr = "".join(dateList)
	return returnStr
# end def

# This function returns the length of the longest key in the dict()
# It takes a dict input and returns an int
def longestName(theDic):
	return max(imap(len, theDic))


inputFile = open("Calendar/DataBase.db", "r")
assignment = dict()    # map from assignment names to due dates

for line in inputFile:
	newString = line.split()          # the first entry is name and the second being date and time
	assignment[newString[0]] = newString[1]    # map a name to date and time
# end for

# sort the dictionary by date and time
assignment = OrderedDict(sorted(assignment.items(), key=lambda x: int(x[1])))
todayDate = int(datetime.today().strftime('%Y%m%d'))  # get today's date

for key in assignment:
	currDate = []          # declare an empty list
	for i in range(8):     # only store date into the list (get rid of time)
		currDate.append(assignment[key][i])
	stringDate = "".join(currDate)       # convert the list into a string
	if int(stringDate) < todayDate:      # if the date is less than today's date
		del assignment[key]              # the assignment has passed due date
		print(key + " is deleted because it has passed the due date")
	# end if
# end for

print("")
# Up to this point, all history have been stored into the dictionary and sorted #

print("Welcome to Todo App developed by James Li.")
print("Today is " + datetime.today().strftime('%Y-%m-%d') + ".")
print("Thanks for using this app. Have a nice one :)")
print("----------------------------------------------")

while True:
	print("Enter \"i\" to insert a new assignment")
	print("Enter \"d\" to delete old assignments")
	print("Enter \"c\" to check the due date of a specific assignment")
	print("Enter \"t\" to get a list of things to do tomorrow")
	print("Enter \"o\" to get a list of things to do today")
	print("Enter \"l\" to get 10 deadline-in-the-ass assignments")
	print("Enter \"r\" to revise the date of a certain assignment")
	ch = raw_input("Press \"q\" to exit\n")
	print("")

	if ch == 'q' or ch == 'Q':
		with open("Calendar/DataBase.db", "w") as f:   # rewrite DataBase.db
			for key in assignment:
				f.write(key + " " + bytes(assignment[key]) + "\n")
		# end for
		break
	elif ch == 'i' or ch == 'I':
		name = raw_input("   1. Enter assignment name\n")
		date = raw_input("   2. Enter the date (format: year + month + day, e.g. 20170318)\n")
		date = re.sub("[^0-9]", "", date)     # keep only numeric chars
		time = raw_input("   3. Enter the time (format: hour + minute, e.g. 15:30\n")
		time = re.sub("[^0-9]", "", time)     # for the convenience of reading from data base, keep only numeric chars
		assignment[name] = date + time        # concatenate date and time
		# sort again, so that the newly inserted shit is at the right place
		assignment = OrderedDict(sorted(assignment.items(), key=lambda x: int(x[1])))
	elif ch == 'd' or ch == 'D':
		tobeDeleted = raw_input("   1. Enter assignment name\n")
		if tobeDeleted in assignment:        # check if the assignment is in the dict
			del assignment[tobeDeleted]      # delete it
			print(tobeDeleted + " is deleted")
		else:                                # if the assignment name does not exist
			print(tobeDeleted + " not found")
		# end if-else
	elif ch == 'c' or ch == 'C':
		name = raw_input("   1. Enter assignment name\n")
		if name in assignment:            # check if the assignment is in the dict
			print(bytes(dateFormat(assignment[name])))    # print the date and time
		else:                             # not found
			print(name + " not found")
		print(" ")
	elif ch == 'r' or ch == 'R':
		name = raw_input("   1. Enter assignment name\n")
		if name in assignment:            # check if the assignment is in the dict
			revisedDate = raw_input("   2. Enter the new date\n")    # get new date
			revisedDate = re.sub("[^0-9]", "", revisedDate)          # keep only numeric chars
			revisedTime = raw_input("   3. Enter the rnew time\n")   # get new time
			revisedTime = re.sub("[^0-9]", "", revisedTime)          # keep only numeric chars
			assignment[name] = revisedDate + revisedTime             # concatenate and store
		else:                             # not found
			print(name + " not found")
		print(" ")
	elif ch == 't' or ch == 'T':
		longest = longestName(assignment)  # get the longest word in the dict
		for key in assignment:
			keyLen = len(key)              # get the length of the current word
			diff = longest - keyLen + 2    # the number of required spaces between name and date
			currDate = []         # declare an empty list
			for i in range(8):    # only store date into it
				currDate.append(assignment[key][i])
			stringDate = "".join(currDate)   # convert the list into string
			if int(stringDate) - todayDate == 1:     # get all assignments due tomorrow
				print(key + diff*" " + bytes(dateFormat(assignment[key])))
		print("")
	elif ch == 'o' or ch == 'O':     # similar to the last one
		longest = longestName(assignment)
		for key in assignment:
			keyLen = len(key)
			diff = longest - keyLen + 2
			currDate = []
			for i in range(8):
				currDate.append(assignment[key][i])
			stringDate = "".join(currDate)
			if int(stringDate) - todayDate == 0:
				print(key + diff*" " + bytes(dateFormat(assignment[key])))
		print("")
	elif ch == 'l' or ch == 'L':
		if len(assignment) == 0:      # there is nothing in the dict
			print("Your to-do list is empty, man.")
			continue
		else:
			longest = longestName(assignment)   # get the length of the longest key
			count = 0                  # a counter used to limit ten print-outs
			for key in assignment:
				keyLen = len(key)       # get the length of current key
				diff = longest - keyLen + 2
				count = count + 1
				if count == 11:      # make sure at most ten shits are printed out
					break
				# edn if
				currDate = []
				for i in range(8):
					currDate.append(assignment[key][i])
				stringDate = "".join(currDate)
				difference = int(stringDate) - todayDate
				if difference == 1:
					print(key + diff * " " + bytes(dateFormat(assignment[key])) + " (tomorrow)")
				elif difference == 0:
					print(key + diff * " " + bytes(dateFormat(assignment[key])) + " (today)")
				else:
					print(key + diff * " " + bytes(dateFormat(assignment[key])) + " (in " + bytes(difference) + " days)")
			# end for
		# end if-else
		print("")
	# end if-else
# end while

inputFile.close()



