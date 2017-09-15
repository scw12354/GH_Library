from core import game

name = 'Fred'
a = 'someeethinggggg'
cortn = game(name,a)
cortn.__next__()
count = 1
flag = 0
#a = 'something'
while True:
    thenum = int(input())
    cortn.send([thenum, count])
            
    print('you did ' + str(count) + ' times')
    count +=1 
    if count == 8:
        print('술1잔!')
    if count == 10:
        print('술2잔!')
    if count == 12:
        print('술3잔!')
    print('\n')

#print('game over')
