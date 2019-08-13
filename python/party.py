import random

while(True):
    rubbish = raw_input()
    if rubbish == "q":
       break
    else:
        print random.randint(1,13)
