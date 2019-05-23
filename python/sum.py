def sum(x):
    return reduce(lambda x,y: x+y, range(0, x+1))


x = input("Enter a positive integer: ")
print(sum(x))
