the_list = [3.1, 3.2, 8.0, 1.2, 3.5, 5.4, 2.1, 4.6, 2.4, 2.4, 1.5, 6.5]
the_list.sort()
median = 0

if(len(the_list)%2==0):     # if the length of the list is an even number
   median = (the_list[int(len(the_list)/2)] + the_list[int(len(the_list)/2)-1]) / 2
else:                       # if it is an odd number
   median = the_list[int(len(the_list)/2)]

print("The list is: " + str(the_list))
print("Median of the list is " + str(round(median, 4)))
