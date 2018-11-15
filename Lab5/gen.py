import random

for i in range(0,300):
    coin = random.random()
    if coin < 0.33:
        print('e '+str(random.randint(1,1000)))
    elif coin < 0.66:
        print('d')
    else:
        print('p')
