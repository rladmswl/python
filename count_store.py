
#자판기 연습
'''
print("〰"*8+"프친 푸드 가게"+"〰"*8)
print('1. 토스트(🍞) 1500원 2. 햄버거세트(🍔🍟🥤) 5300원 3. 피자(🍕) 9900원')

money = int(input("금액>>"))
menu = int(input("메뉴선택>>"))

if menu==1:
    money -= 1500
elif menu==2:
    money -= 5300
elif menu==3:
    money -= 9900
    
if money < 0:
    print("금액이 부족합니다")
else:
    won1000 = money//1000
    won500 = money%1000//500
    won100 = money%1000%500//100
    print("거스름돈: 1000원 {}개, 500원 {}개, 100원 {}개".format(won1000, won500, won100))
'''

#주사위게임
'''
import random

for i in range(0,10):
    d=random.randint(1,6)
    print(d)
'''

import random

d1=random.randint(1,6)
d2=random.randint(1,6)

if d1>d2:
    print('i win')
else:
    print('computer win')






















