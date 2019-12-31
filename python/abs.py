def abs(x):
   y = x >> 31
   return (x + y) ^ y

a = -10
print(abs(a))
b = 13
print(abs(b))
