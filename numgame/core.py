import random

def game(name):
    print("hello " + name)
    print('input an integer 0<num<101')
    num = random.randrange(1,101)
    while True:
        inum = (yield)
        if inum < 0 or inum > 100:
            print("Error, please input a number between 1 and 100")
        elif inum > num:
            print("too big")
        elif inum < num:
            print("too small")
        else: 
            print('Correct!')

