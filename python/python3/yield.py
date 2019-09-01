def print_even(test_string):
   for i in test_string:
      if i == "geeks":
         yield i

# initializing string
test_string = " The are many geeks around you, \
              geeks are known for teaching other geeks"

# printing even numbers using yield
count = 0
print ("The number of geeks in string is : ", end = "" )
test_string = test_string.split()

#  print(len(print_even(test_string)))
# The above line does not work because the returned value of print_even is 'generater'

for j in print_even(test_string):
   count += 1

print(count)

