import random
import sys

while(True):
    rubbish = raw_input()
    if rubbish == "q":
        sys.exit()
    else:
        print random.randint(1,14)
