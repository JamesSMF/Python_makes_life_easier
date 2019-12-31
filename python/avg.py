def avg(x, y):
   # x & y calculates carry out
   # x ^ y calculates the actual value (0 or 1)
   # shifting right by 1 equals to dividing the number by 2
   return (x & y) + ((x ^ y) >> 1)

a = 10
b = 17
print(avg(a, b))
a = 103
b = 47
print(avg(a, b))
