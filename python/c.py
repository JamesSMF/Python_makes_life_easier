# DataBase Format: <datetime> + <event>

from collections import OrderedDict
from datetime import datetime, date, time, timedelta
from itertools import imap
import re

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	WHITE = '\033[97m'
	PERFECTBLUE = '\033[96m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

# Given a date, it finds the next weekday (e.g. next Monday).
# d: datetime       weekday: int           return: datetime
def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + timedelta(days_ahead)

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

# This function returns the length of the longest value in the dict()
# It takes a dict input and returns an int
def longestName(theDic):
	longest = max(theDic.values(), key=len)
	return len(longest)

# This function lists all events out
def listEvents():
	# save the process first ----------------------
	with open("Calendar/DataBase.db", "w") as f:   # rewrite DataBase.db
		for key in assignment:
			f.write(key + " " + bytes(assignment[key]) + "\n")
		# end for
	# end with

	print ""
	if len(assignment) == 0:      # there is nothing in the dict
		print bcolors.WARNING + "Your to-do list is empty, man." + bcolors.ENDC
		return
	else:
		longest = longestName(assignment)   # get the length of the longest key
		count = 0                  # a counter used to limit ten print-outs
		# key is the date, and you are enumerating dates in the dict()
		for key in assignment:
			keyLen = len(assignment[key])       # get the length of current event
			diff = longest - keyLen + 2
			count = count + 1
			if count == 17:      # make sure at most 16 shits are printed out
				break
			# end if

			todayYear = list()
			currYear = list()
			todayMon = list()
			currMon = list()
			todayDay = list()
			currDay = list()
			for i in range(8):
				if i<4:
					todayYear.append(str(todayDate)[i])
					currYear.append(key[i])
				elif i<6:
					todayMon.append(str(todayDate)[i])
					currMon.append(key[i])
				else:
					todayDay.append(str(todayDate)[i])
					currDay.append(key[i])
			# end for

			fuckCurrYear = "".join(currYear)
			fuckTodayYear = "".join(todayYear)
			fuckCurrMon = "".join(currMon)
			fuckTodayMon = "".join(todayMon)
			fuckCurrDay = "".join(currDay)
			fuckTodayDay = "".join(todayDay)

			delta = date(int(fuckCurrYear), int(fuckCurrMon), int(fuckCurrDay)) - date(int(fuckTodayYear), int(fuckTodayMon), int(fuckTodayDay))
			difference = int(delta.days)

			# create a set of event names in weekly calendar
			nextWeek = open("Calendar/Weekly.db", "r")
			listWeek = set()
			for ddd in nextWeek:
				listWeek.add(ddd.split()[2])
			nextWeek.close()

			weekdayCode = datetime.strptime(key, "%Y%m%d%H%M").weekday()
			wdaydict = {0:'Mon ',1:'Tues',2:'Wed ',3:'Thur',4:'Fri ',5:'Sat ',6:'Sun '}
			if difference == 1:
				if assignment[key] in listWeek:
					print(assignment[key] + diff * " " + bytes(dateFormat(key)) + ' ' + wdaydict[weekdayCode] + " (tomorrow)")
				else:
					print bcolors.WARNING + (assignment[key] + diff * " " + bytes(dateFormat(key)) + ' ' + wdaydict[weekdayCode] + " (tomorrow)") + bcolors.ENDC
			elif difference == 0:
				if assignment[key] in listWeek:
					print(assignment[key] + diff * " " + bytes(dateFormat(key)) +' ' + wdaydict[weekdayCode] + " (today)")
				else:
					print bcolors.WARNING+ (assignment[key] + diff * " " + bytes(dateFormat(key)) +' ' + wdaydict[weekdayCode] + " (today)") + bcolors.ENDC
			else:
				if assignment[key] in listWeek:
					print(assignment[key] + diff * " " + bytes(dateFormat(key)) + ' ' + wdaydict[weekdayCode] +  " (in " + bytes(difference) + " days)")
				else:
					print bcolors.WARNING+ (assignment[key] + diff * " " + bytes(dateFormat(key)) + ' ' + wdaydict[weekdayCode] +  " (in " + bytes(difference) + " days)") + bcolors.ENDC
		# end for
	# end if-else
	print("")


inputFile = open("Calendar/DataBase.db", "r")
assignment = dict()    # restructured: map from due dates to assignment

for line in inputFile:
	newString = line.split()      # split lines in database by space
	the_name_of_assignment = ' '.join(newString[1:])     # newString[0] is date and time
	assignment[newString[0]] = the_name_of_assignment    # map date and time to name
# end for

# get today's date
tDate = datetime.today()
todayDate = int(tDate.strftime('%Y%m%d'))

# push next week's agenda in
nextWeek = open("Calendar/Weekly.db", "r")
for line in nextWeek:
	newString = line.split()
	# get the the date of the last class in next week
	nextShit = next_weekday(datetime.today(), int(newString[0]))
	# stripe it into %Y%m%d form
	# String nextDay;
	nextDay = nextShit.strftime('%Y%m%d')
	# String parseTime;
	parseTime = datetime.strptime(nextDay, "%Y%m%d")
	catDay = str(nextDay) + newString[1]
	reDay = re.sub("[^0-9]", "", catDay)

	assignment[reDay] = newString[2]
# end for

# sort the dictionary by date and time
assignment = OrderedDict(sorted(assignment.items(), key=lambda x: int(x[0])))

# delete expired assignments
# key is the date
for key in assignment:
	stringDate = key[:8]       # take out YMD only
	copy = assignment[key]
	if int(stringDate) < todayDate:      # if the date is less than today's date
		del assignment[key]               # the assignment has passed due date
		print bcolors.WHITE + (copy + " is automatically deleted because it has passed the due date") + bcolors.ENDC
	# end if
# end for

print("")
# Up to this point, all history date have been stored into the dictionary and sorted #
#  bcolors.WARNING + bcolors.BOLD + "map succeeded" + bcolors.ENDC
print bcolors.HEADER + "Welcome to Todo App developed by James Li." + bcolors.ENDC
print bcolors.HEADER +("Today is " + datetime.today().strftime('%Y-%m-%d') + ".") + bcolors.ENDC
print bcolors.HEADER +"Thanks for using this app. Have a nice one :)" + bcolors.ENDC
print bcolors.HEADER + "----------------------------------------------" + bcolors.ENDC

while True:
	assignment = OrderedDict(sorted(assignment.items(), key=lambda x: int(x[0])))
	print bcolors.PERFECTBLUE + "Commands: ls, map, rm, mv, i, o, q, t, c, r, d" + bcolors.ENDC
	print bcolors.PERFECTBLUE + "Detailed instructions are in the README file." + bcolors.ENDC
	print bcolors.PERFECTBLUE + "Please enter your operation:" + bcolors.ENDC
	ch = raw_input("")
	charArray = ch.split()    # input array: get usr input

	if len(charArray)==0:
		# sort the dict
		assignment = OrderedDict(sorted(assignment.items(), key=lambda x: int(x[0])))
		continue
	elif charArray[0] == 'q' or charArray[0] == 'Q' or charArray[0] == "exit" or charArray[0] == "quit" or charArray[0] == "ZZ":
		with open("Calendar/DataBase.db", "w") as f:   # rewrite DataBase.db
			# key is the date
			for key in assignment:
				f.write(key + " " + bytes(assignment[key]) + "\n")
			# end for
		break
	elif (charArray[0] == 'i' or charArray[0] == 'I') and len(ch)==1:
		name = raw_input("   1. Enter assignment name\n")
		Date = raw_input("   2. Enter the date (format: year + month + day, e.g. 20170318)\n")
		if Date == "today" or Date=='':
			Date = datetime.today().strftime('%Y%m%d')
		elif Date == "tomorrow":
			Date = str(date.today() + timedelta(days=1))
		Date = re.sub("[^0-9]", "", Date)     # keep only numeric chars
		# validity check
		if len(Date) != 8:
			print "Please enter a valid date.\n"
			continue
		time = raw_input("   3. Enter the time (format: hour + minute, e.g. 15:30\n")
		time = re.sub("[^0-9]", "", time)     # for the convenience of reading from data base, keep only numeric chars
		if len(time) != 4:
			time = "0000"
		assignment[Date + time] = name        # concatenate date and time
	elif charArray[0] == 'd' or charArray[0] == 'D':
		tobeDeleted = raw_input("   1. Enter assignment name\n")
		if tobeDeleted in assignment.values():        # check if the assignment is in the dict
			for key in list(assignment.keys()):
				if assignment[key]==tobeDeleted:
					del assignment[key]
			print bcolors.FAIL + (tobeDeleted + " is deleted") + bcolors.ENDC
		else:                                # if the assignment name does not exist
			print(tobeDeleted + " not found")
		# end if-else
	elif charArray[0]=='rm' or charArray[0]=='delete':
		splitedCH = ch.split()[1:]   # for every item after 'rm'
		itemToDel = ' '.join(splitedCH)
		if itemToDel in assignment.values():  # if it is in the event dict
			for key in list(assignment.keys()):
				if assignment[key]==itemToDel:
					del assignment[key]
					print bcolors.FAIL +  (itemToDel + " is deleted") + bcolors.ENDC
		else:
				print(itemToDel + " not found")
		print('')
	elif charArray[0] == 'c' or charArray[0] == 'C':
		name = raw_input("   1. Enter assignment name\n")
		if name in assignment.values():            # check if the assignment is in the dict
			print(bytes(dateFormat(assignment[name])))    # print the date and time
		else:                             # not found
			print(name + " not found")
		print(" ")
	elif charArray[0]=='mv':
		if len(charArray)!= 3:         # takes three arguments
			print("mv <old event name> <new name>")
			continue
		if charArray[1] not in assignment.values():
			print(charArray[1] + " not found")
			continue
		date_of_old = assignment.keys()[assignment.values().index(charArray[1])]  # get the date of old
		assignment[date_of_old] = charArray[2]   # map new name to old date
		print("")
	elif charArray[0] == 'r' or charArray[0] == 'R':
		name = raw_input("   1. Enter assignment name\n")
		if name in assignment.values():            # check if the assignment is in the dict
			revisedDate = raw_input("   2. Enter the new date\n")    # get new date
			revisedDate = re.sub("[^0-9]", "", revisedDate)          # keep only numeric chars
			revisedTime = raw_input("   3. Enter the rnew time\n")   # get new time
			revisedTime = re.sub("[^0-9]", "", revisedTime)          # keep only numeric chars
			assignment[revisedDate + revisedTime] = name             # concatenate and store
		else:                             # not found
			print(name + " not found")
		print(" ")
	elif charArray[0] == 't' or charArray[0] == 'T':
		longest = longestName(assignment)  # get the longest word in the dict
		# key is the date
		for key in assignment:
			keyLen = len(assignment[key])  # get the length of the current event name
			diff = longest - keyLen + 2    # the number of required spaces between name and date
			stringDate = key[:8]           # keep only YMD
			if int(stringDate) - todayDate == 1:     # get all assignments due tomorrow
				print(assignments[key] + diff*" " + bytes(dateFormat(key)))
		print("")
	elif charArray[0] == 'o' or charArray[0] == 'O':     # similar to the last one
		longest = longestName(assignment)       # get the longest event name
		for key in assignment:
			keyLen = len(assignment[key])
			diff = longest - keyLen + 2
			stringDate = key[:8]
			if int(stringDate) - todayDate == 0:
				print(assignment[key] + diff*" " + bytes(dateFormat(key)))
		print("")
	elif charArray[0]=="more":
		if len(assignment)==0:
			print bcolors.WARNING + "Your to-do list is empty, man." + bcolors.ENDC
			continue
		else:
			longest = longestName(assignment)
			for key in assignment:
				keyLen = len(assignment[key])
				diff = longest - keyLen + 2
				todayYear = list()
				todayYear = list()
				currYear = list()
				todayMon = list()
				currMon = list()
				todayDay = list()
				currDay = list()
				for i in range(8):
					if i<4:
						todayYear.append(str(todayDate)[i])
						currYear.append(key[i])
					elif i<6:
						todayMon.append(str(todayDate)[i])
						currMon.append(key[i])
					else:
						todayDay.append(str(todayDate)[i])
						currDay.append(key[i])
             # end for

				fuckCurrYear = "".join(currYear)
				fuckTodayYear = "".join(todayYear)
				fuckCurrMon = "".join(currMon)
				fuckTodayMon = "".join(todayMon)
				fuckCurrDay = "".join(currDay)
				fuckTodayDay = "".join(todayDay)

				delta = date(int(fuckCurrYear), int(fuckCurrMon), int(fuckCurrDay)) - date(int(fuckTodayYear),     int(fuckTodayMon), int(fuckTodayDay))
				difference = int(delta.days)

				# create a set of event names in weekly calendar
				nextWeek = open("Calendar/Weekly.db", "r")
				listWeek = set()
				for ddd in nextWeek:
					listWeek.add(ddd.split()[2])
				nextWeek.close()

				weekdayCode = datetime.strptime(key, "%Y%m%d%H%M").weekday()
				wdaydict = {0:'Mon ',1:'Tues',2:'Wed ',3:'Thur',4:'Fri ',5:'Sat ',6:'Sun '}
				if difference == 1:
					if assignment[key] in listWeek:
						print(assignment[key] + diff * " " + bytes(dateFormat(key)) + ' ' + wdaydict[weekdayCode] +  " (tomorrow)")
					else:
						print bcolors.WARNING + (assignment[key] + diff * " " + bytes(dateFormat(key)) + ' ' + wdaydict[weekdayCode] + " (tomorrow)") + bcolors.ENDC
				elif difference == 0:
					if assignment[key] in listWeek:
						print(assignment[key] + diff * " " + bytes(dateFormat(key)) +' ' + wdaydict[weekdayCode] +   " (today)")
					else:
						print bcolors.WARNING+ (assignment[key] + diff * " " + bytes(dateFormat(key)) +' ' + wdaydict[weekdayCode] + " (today)") + bcolors.ENDC
				else:
					if assignment[key] in listWeek:
						print(assignment[key] + diff * " " + bytes(dateFormat(key)) + ' ' + wdaydict[weekdayCode] +  " (in " + bytes(difference) + " days)")
					else:
						print bcolors.WARNING+ (assignment[key] + diff * " " + bytes(dateFormat(key)) + ' ' +  wdaydict[weekdayCode] +  " (in " + bytes(difference) + " days)") + bcolors.ENDC
			# end for
		#end if-else
		print ''
	elif charArray[0] == 'l' or charArray[0] == 'L' or charArray[0] == "ls":
		listEvents()
	elif charArray[0]=='map':
		# if the time is like 3:00, it will be converted to 15:00
		charArray[-1] = re.sub("[^0-9]", "", charArray[-1])
		if len(charArray[-1])==3 and int(charArray[-1][0])<6:
			charArray[-1] = str(int(charArray[-1])+1200)

		if charArray[-2]=="today":
			Date = datetime.today().strftime('%Y%m%d')
			Date = Date + str(charArray[-1])
		elif charArray[-2]=='tomorrow':
			Date = str(date.today() + timedelta(days=1))
			Date = Date + str(charArray[-1])
		elif charArray[-2]=="Sun" or charArray[2]=="Sunday":
			# String nextDate;
			nextDate = next_weekday(datetime.today(), 6).strftime('%Y%m%d')
			Date = nextDate + str(charArray[-1])
		elif charArray[-2]=="Mon" or charArray[2]=="Monday":
			# String nextDate;
			nextDate = next_weekday(datetime.today(), 0).strftime('%Y%m%d')
			Date = nextDate + str(charArray[-1])
		elif charArray[-2]=="Tues" or charArray[2]=="Tuesday":
			# String nextDate;
			nextDate = next_weekday(datetime.today(), 1).strftime('%Y%m%d')
			Date = nextDate + str(charArray[-1])
		elif charArray[-2]=="Wed" or charArray[2]=="Wednesday":
			# String nextDate;
			nextDate = next_weekday(datetime.today(), 2).strftime('%Y%m%d')
			Date = nextDate + str(charArray[-1])
		elif charArray[-2]=="Thur" or charArray[2]=="Thurs" or charArray[2]=="Thursday":
			# String nextDate;
			nextDate = next_weekday(datetime.today(), 3).strftime('%Y%m%d')
			Date = nextDate + str(charArray[-1])
		elif charArray[-2]=="Fri" or charArray[2]=="Friday":
			# String nextDate;
			nextDate = next_weekday(datetime.today(), 4).strftime('%Y%m%d')
			Date = nextDate + str(charArray[-1])
		elif charArray[-2]=="Sat" or charArray=='Saturday':
			# String nextDate;
			nextDate = next_weekday(datetime.today(), 5).strftime('%Y%m%d')
			Date = nextDate + str(charArray[-1])
		else:
			if(len(charArray[-1])==12):
				Date = charArray[-1]
			else:
				Date = ''.join(charArray[-2:])
		Date = re.sub("[^0-9]", "", Date)     # keep only numeric chars
		if len(Date)==4:
			Date = datetime.today().strftime('%Y%m%d') + Date
		if len(Date) != 12:
			print("Please enter a valid date.\n")
			continue

		# new feature for version 2.3.1: time conflict check
		flag = True
		for datE in assignment:
			targetTime = datetime.strptime(datE, "%Y%m%d%H%M") # datetime type
			compTime = datetime.strptime(Date, "%Y%m%d%H%M")   # datetime type
			diffTime = compTime - targetTime      # calculate the time difference
			if diffTime<timedelta(minutes=0):     # absolute value
				diffTime = -diffTime
			if diffTime <= timedelta(minutes=60): # if the absolute value of difference is less than an hour
				print("\n" + str(assignment[datE]) + " is "+ datE)     # print warning message
				ans =raw_input("Are you sure want to insert the event? (y/n)\n")
				if ans=="y" or ans=="yes" or ans=='' or ans=='yup' or ans=='yeah' or ans=='Hell Yeah' or ans=='hell yeah':
					continue
				else:
					flag = False
					break
		# end for
		if flag:    # if approved to insert the event
			if len(charArray[-1])==12:  # if regular format of date
				assignment[Date] = ' '.join(charArray[1:-1])
			elif len(charArray)==3:     # simplified entry
				assignment[Date] = ' '.join(charArray[1:-1])
			else:                       # if not regular (by date code)
				assignment[Date] = ' '.join(charArray[1:-2])
			print bcolors.WARNING + bcolors.BOLD + "map succeeded" + bcolors.ENDC
		print('')
		# end if
	else:       # None of the previous patterns are matched
		if re.search("today's date", ch) or re.search("date of today", ch) or re.search("date today", ch):
			print("Today is " + datetime.today().strftime('%Y-%m-%d') + ".")
		elif re.search("Fuck", ch) or re.search("Bustard", ch) or re.search("asshole", ch) or re.search("shit", ch) or re.search("whore", ch):
			print("No bad words, bitch.")
		elif re.search("agenda", ch) or re.search('schedule', ch) or re.search("calendar", ch) or re.search("my plan", ch) or re.search("My plan", ch) or re.search("Schedule", ch) or re.search("Agenda", ch) or re.search("Calendar", ch):
			listEvents()
		elif re.search("I will", ch) or re.search("I want to", ch) or re.search("I plan to", ch) or re.search("I intend to", ch) or re.search("to my plan", ch) or re.search("to my schedule",ch):
			ch = re.sub("to my schedule", "", ch)
			ch = re.sub("I want to", "", ch)
			ch = re.sub("I intend to", "", ch)
			ch = re.sub("I will", "", ch)
			ch = re.sub("I plan to", "", ch)
			ch = re.sub("to my plan", "", ch)

			if re.search("tomorrow",ch):
				ch = re.sub("tomorrow","",ch)      # delete "tomorrow"
				Date = str(date.today() + timedelta(days=1))

			ch = re.sub("[^A-Za-z0-9 ]", "", ch)
			timeList=list()
			splitedList = ch.split()
			for s in range(0, len(ch.split())):
				if splitedList[s].isdigit():
					timeList.append(splitedList[s])
					if(splitedList[s-1]=="at" or splitedList[s-1]=="on" or splitedList[s-1]=="in" or splitedList[s-1]=="during"):
						splitedList.pop(s-1)
					break

			ch = " ".join(splitedList)
			if(len(timeList)>2):
				print "Please enter a valid time\n"
				continue

			exactTime = "".join(str(x) for x in timeList)
			Date = Date + str(exactTime)
			Date = re.sub("[^0-9]", "", Date)
			if len(Date)==4:
				Date = datetime.today().strftime('%Y%m%d') + Date

			if len(Date)!=12:
				print("Please enter a valid date.\n")
				continue

			eventName = re.sub("[^a-zA-Z ]", "", ch);
			eventName = eventName.strip()

		# new feature for version 2.3.1: time conflict check
			flag = True
			for datE in assignment:
				targetTime = datetime.strptime(datE, "%Y%m%d%H%M") # datetime type
				compTime = datetime.strptime(Date, "%Y%m%d%H%M")   # datetime type
				diffTime = compTime - targetTime      # calculate the time difference
				if diffTime<timedelta(minutes=0):     # absolute value
					diffTime = -diffTime
				if diffTime <= timedelta(minutes=60): # if the absolute value of difference is less than an hour
					print("\n" + str(assignment[datE]) + " is "+ datE)     # print warning message
					ans =raw_input("Are you sure want to insert the event? (y/n)\n")
					if ans=="y" or ans=="yes" or ans=='' or ans=='yup' or ans=='yeah' or ans=='Hell Yeah' or ans=='hell yeah':
						continue
					else:
						flag = False
						break
			# end for

			if flag:    # if approved to insert the event
				assignment[Date] = eventName
			print bcolors.WARNING + bcolors.BOLD + "map succeeded" + bcolors.ENDC
			print('')
			# end if

		elif charArray[0]=='I':
			ch = re.sub("\.", "", ch)
			ch += ", too."
			print ch
		else:
			ch = re.sub("\?", "!", ch)
			ch = re.sub("What's your name", "I am ToDo App", ch)
			ch = re.sub("What is your name", "I am ToDo App", ch)
			ch = re.sub("Who are you", "I am ToDo App", ch)
			ch = re.sub("What can you do", "I can do anything", ch)

			ch = re.sub("Are you", "Yes, I am", ch)
			ch = re.sub("are you", "am I", ch)
			ch = re.sub("Can you", "I can", ch)
			ch = re.sub("you are", "I am", ch)
			ch = re.sub("You are", "I am", ch)
			ch = re.sub("Is that", "That is", ch)
			ch = re.sub("Is it", "It is", ch)

			ch = re.sub("Your", "My", ch)
			ch = re.sub("your", "my", ch)
			ch = re.sub("You", "I", ch)
			ch = re.sub("you", "I", ch)
			ch = re.sub(" me", " you", ch)
			ch = re.sub("No", "Yes", ch);
			print ch
		print ""    # print a newline

	# end if-else
# end while

inputFile.close()
nextWeek.close()


