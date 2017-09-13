from core import game

name = 'Fred'

cortn = game(name)
cortn.next()
count = 0
while True:
    thenum = int(raw_input())
    if cortn.send(thenum) == 'Correct!':
        cortn.close()
        break
        
    print('you did ' + str(count) + ' times')
    count +=1 
print('game over')
