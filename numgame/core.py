import random

def game(name,a):
    print("hello " + name)
    print('input an integer 0<num<101')
    num = random.randrange(1,101)
    while True:
        flag = 0
        numm = (yield)
        inum = int(numm[0])
        count = int(numm[1])
        if inum < 0 or inum > 100:
            print("Error, please input a number between 1 and 100")
        elif inum > num:
            print("too big")
            
        elif inum < num:
            print("too small")
            
        else: 
            print('Correct!')
            if count <= 7:
                print('술먹일 사람 선!택!')
            break

           
            

