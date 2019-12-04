"""
CRAPS 赌博游戏

Version: 0.1
Author: Cedar43
Date: 2019-12-04
"""
from random import randint

money = 1000
while money > 0:
    print('You still have $%d' % money)
    needs_go_on = False
    while True:
        debt = int(input('Debt:'))
        if 0 < debt <= money:
            break
        else:
            print('You dont have enough money! Please try again')
    first = randint(1, 6) + randint(1, 6)
    print('first round:', first)
    if first == 7 or first == 11:
        print('Congratulations! You win!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('Sorry,you lose')
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('another round:', current)
        if current == 7:
            print('Sorry,you lose')
            money -= debt
        elif current == first:
            print('Congratulations! You win!')
            money += debt
        else:
            needs_go_on = True
print('Now you dont have enough money to continue.')
