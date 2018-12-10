from collections import OrderedDict

inputFile = open("DataBase.txt", "r")
assignment = dict()    # map from assignment names to due dates

for line in inputFile:
	newString = line.split()          # the first entry is name and the second being date
	assignment[newString[0]] = newString[1]    # map a name to date
# end for

assignment = OrderedDict(sorted(assignment.items(), key=lambda x: int(x[1])))  # sort the dictionary by due date

# Up to this point, all history have been stored into the dictionary and sorted #

print("Welcome to Calendar App developed by James Li.")
print("----------------------------------------------")

while True:
	print("Enter \"i\" to insert a new assignment")
	print("Enter \"d\" to delete old assignments")
	print("Enter \"c\" to check the due date of a certain assignment")
	print("Enter \"r\" to get 10 due-soon assignments")
	ch = raw_input("Press \"q\" to exit\n")

	if ch == 'q' or ch == 'Q':
		with open("DataBase.txt", "w") as f:   # rewrite DataBase.txt
			for key in assignment:
				f.write(key + " " + bytes(assignment[key]) + "\n")
		# edn for
	# end if
		break
	elif ch == 'i' or ch == 'I':
		name = raw_input("   1. Enter assignment name\n")
		date = raw_input("   2. Enter the date (form: year + month + day, e.g. 20170318)\n")
		assignment[name] = date
		assignment = OrderedDict(sorted(assignment.items(), key=lambda x: int(x[1])))
	elif ch == 'd' or ch == 'D':
		tobeDeleted = raw_input("   1. Enter assignment name\n")
		del assignment[tobeDeleted]
	elif ch == 'c' or ch == 'C':
		name = raw_input("   1. Enter assignment name\n")
		print(bytes(assignment[name]))
		print(" ")
	elif ch == 'r' or ch == 'R':
		if len(assignment) <= 10:      # if there are less than 10 items in the dict
			for key in assignment:
				print (key + " " + bytes(assignment[key]))
			# end for
			print("")
		else:                    # if there are too many items in the dict, print first 10
			count = 0
			for key in assignment:
				count = count + 1
				if count == 10:
					break
				# edn if
				print (key + " " + bytes(assignment[key]))
			# end for
		# end if-else



