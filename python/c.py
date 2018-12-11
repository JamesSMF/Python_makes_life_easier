from collections import OrderedDict
from datetime import datetime

inputFile = open("Calendar/DataBase.db", "r")
assignment = dict()    # map from assignment names to due dates

for line in inputFile:
	newString = line.split()          # the first entry is name and the second being date
	assignment[newString[0]] = newString[1]    # map a name to date
# end for

assignment = OrderedDict(sorted(assignment.items(), key=lambda x: int(x[1])))  # sort the dictionary by due date
todayDate = int(datetime.today().strftime('%Y%m%d'))

for key in assignment:
    if int(assignment[key]) < todayDate:
		del assignment[key]
		print(key + " is deleted because it passed due date")
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
	print("Enter \"r\" to get 10 deadline-in-the-ass assignments")
	ch = raw_input("Press \"q\" to exit\n")

	if ch == 'q' or ch == 'Q':
		with open("Calendar/DataBase.db", "w") as f:   # rewrite DataBase.db
			for key in assignment:
				f.write(key + " " + bytes(assignment[key]) + "\n")
		# edn for
	# end if
		break
	elif ch == 'i' or ch == 'I':
		name = raw_input("   1. Enter assignment name\n")
		date = raw_input("   2. Enter the date (format: year + month + day, e.g. 20170318)\n")
		assignment[name] = date
		assignment = OrderedDict(sorted(assignment.items(), key=lambda x: int(x[1])))
	elif ch == 'd' or ch == 'D':
		tobeDeleted = raw_input("   1. Enter assignment name\n")
		if tobeDeleted in assignment:
			del assignment[tobeDeleted]
			print(tobeDeleted + " is deleted")
		else:
			print(tobeDeleted + " not found")
			continue
	elif ch == 'c' or ch == 'C':
		name = raw_input("   1. Enter assignment name\n")
		if name in assignment:
			print(bytes(assignment[name]))
			print(" ")
		else:
			print(name + " not found")
	elif ch == 't' or ch == 'T':
		for key in assignment:
			if int(assignment[key]) - todayDate == 1:
				print(key + " " + bytes(assignment[key]))
	elif ch == 'o' or ch == 'O':
		for key in assignment:
			if int(assignment[key]) - todayDate == 0:
				print(key + " " + bytes(assignment[key]))
	elif ch == 'r' or ch == 'R':
		if len(assignment) == 0:
			print("Your to-do list is empty, man.")
			continue
		elif len(assignment) <= 10:      # if there are less than 10 items in the dict
			for key in assignment:
				difference = int(assignment[key]) - todayDate
				if difference == 1:
					print(key + " " + bytes(assignment[key]) + " (tomorrow)")
				elif difference == 0:
					print(key + " " + bytes(assignment[key]) + " (today)")
				else:
				    print(key + " " + bytes(assignment[key]) + " (in " + bytes(difference) + " days)")
			# end for
		else:                    # if there are too many items in the dict, print first 10
			count = 0
			for key in assignment:
				count = count + 1
				if count == 11:
					break
				# edn if
				print (key + " " + bytes(assignment[key]))
			# end for
		# end if-else
		print("")
	# end if-else
# end while



