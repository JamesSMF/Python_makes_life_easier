import sys

def factorial(x):
   if(not x.isdigit()):
      return -1
   return reduce(lambda x,y: x * y, [1]+range(1, int(x)+1))
   # prepend a [1] to prevent the input being 0

inp = raw_input("please enter the number: ")

out = factorial(inp)
if(out==-1):
   print("Please enter a valid number.")
else:
   print(out)
