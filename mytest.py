
#if 문-수 비교
'''
if 10 > 11 :
    print("10은 11보다 크다")
else:
    print("10은 11보다 작다")
'''

#if문-수 비교2
'''
a=10
b=11
if a>b:
    print("a는 b보다 크다")
else:
    print("a는 b보다 작다")
'''

#while문-1부터 5까지 출력
'''
a=1
while a<=5:
    print(a)
    a+=1
'''

#while문2-1부터5까지 더하기
'''
a=1
sum=0
while a<=5:
    print(a)
    sum=sum+a
    a+=1  # sum 앞에 오면 안됨. 더하고 a값을 올려야함. 안그러면 오류.
print(sum)
'''

#for문
'''
for c in [5,7,9]:
    print(c)
'''

#for문
'''
a=[5,7,9]
b=0
for c in a:
    b=b+c
    print(b)
'''

#input문
'''
a=input()
'''

#인덱스*************************  -> mystr 오류 ㅠㅡㅠ
'''
#a="abcdef"
#mystr[2]
'''

#문자열 포매팅
'''
age=23
print("I am %d years old" % age)  # ~ old", % ~ 하면 안됨!  , 오류남
'''

#리스트
'''
rainbow=['빨', '주', '노', '초', '파', '남', '보']
print(rainbow)
'''

# 리스트 추가 삭제
'''
c=[]    # 빈 배열 생성
c.append('kim')
c.append('lee')
c.append('park')    # 자료 추가
print(c)
c.insert(1,'hong')    # 특정 위치에 추가
print(c)
c.remove('lee')    # 자료 명으로 삭제
print(c)
del c[1]    # 인덱스로 삭제
print(c)
'''

# '안녕'이라고 말해줘
'''
print('안녕')
'''

# 20에 30을 더하면? 평균은?
'''
a=20
b=30
c=a+b
print(c)
print(c/2)
'''

# 숫자를 입력받아 홀수인지 짝수인지 구별
'''
a=int(input())  # a=input()으로 하면 오류남! 
if a%2==0:
    print("a는 짝수이다.")
else:
    print("a는 홀수이다.")
'''

# 100원, 10원, 1원 3가지 동전으로 1000원을 받은 후
# 648원을 계산한 후 거스름돈 352원을 남겨줄 때,
# 동전의 개수를 가장 적게 거슬러주는 방법은?
'''
x=352
m100=0
m10=0
m1=0

while x>=100:
    m100+=1
    x=x-100 
while x>=10:
    m10+=1
    x=x-10
while x>=1:
    m1+=1
    x=x-1
print(m100, m10, m1)
'''

#나이가 (17, 14, 18, 13, 19) 인 사람들이 있는데 나이가 13인 사람이 있는가?
'''
agelist=[17, 14, 18, 13, 19]
ans='no'
for age in range(0,5):
    if agelist[age]==13:
        ans='yes'
print(ans)      
'''

#나이가 (17, 14, 18, 13, 19) 인 사람들이 있는데 가장 나이가 많은 값 얼마인가?
'''
agelist=[17, 14, 18, 13, 19]
maxage=0
for i in range(0,5):
    if agelist[i]>maxage:
        maxage=agelist[i]
print(maxage)
'''

#나이가 (17, 14, 18, 13, 19) 인 사람들이 있는데 나이순으로 알려다오. **********************
'''
agelist=[17, 14, 18, 13, 19]
for k in range(0,5):
    min=agelist[k]
    minpos=k
    for j in range(k,5):
        if agelist[j]<=min:
            min=agelist[j]
            minpos=j # 이거 왜 쓰는지
    min=agelist[minpos]; agelist[minpos]=agelist[k]; agelist[k]=min
    # 왜 agelist[j]가 아니고 agelist[minpos]인지
    # j는 for j in range()에서 이미 끝났기 때문에 minpos=j로 인해 j가 아닌 minpos를 씀.
    # 밖에서 j를 쓸 수 없기 때문에 minpos에 j를 담아 둔 것이다.
print(agelist)    
'''
#
'''
agelist=[17, 14, 18, 13, 19]
for k in range(0,5):
    min=agelist[k]
    minpos=k
    #print(k)
    #print(min)
    #print(minpos)
    for j in range(k,5):
        if agelist[j]<=min:
            min=agelist[j]
            minpos=j
            #print(min)
            #print(minpos)
    min=agelist[minpos]; agelist[minpos]=agelist[k]; agelist[k]=min
    #print(min)
print(agelist)  
'''

# 커피주문
'''
def order():
    print("주문하실 음료를 알려주세요")
    drink=input()
    return drink

order1=order()
order2=order()
order3=order()

print(order1, order2, order3, '주문하셨습니다.')
'''

# 1부터 n까지 더하기
'''
n=10
mysum=0
for i in range(1,n+1):
    mysum=mysum+i
print(mysum)

##
n=20
mysum=0
for i in range(1, n+1):
    mysum=mysum+i
print(mysum)

#

n=0
def tsum(n):
    mysum=0
    for i in range(1, n+1):
        mysum=mysum+i
    print(mysum)

tsum(10)
tsum(20)
tsum(30)
'''

# 리스트 원소 더하기
'''
def listsum(mylist):
    mysum=0
    for i in mylist:
        mysum+=i
    return mysum    

mylist=[10,20,30]
s=listsum(mylist)
print(s)
'''

# 리스트 원소에서 10 찾기
'''
mylist=[2,6,9,10,7,1]
ans='없다'
for i in range(0,6):
    if mylist[i]==10:
        ans='찾았다'
print(ans)    
'''

# 리스트에서 가장 큰 원소 찾기
'''
mylist=[2,6,9,10,7,1]
max=0
for i in range(0,6):
    if max<mylist[i]:
        max=mylist[i]
print(max)
'''

#
'''
def tbig(mylist,n):
    mybig=0
    for i in mylist:
        if(mybig<i):
            mybig=i
    return(mybig)

mylist=[40, 30, 60, 10, 50]
t=tbig(mylist,35);
print(t)
'''

#
'''
def tbig(mylist):
    mybig=mylist[1]
    for i in mylist:
        if(mybig<i):
            mybig=i
    return(mybig)

mylist=[40, 30, 60, 10, 50]
t=tbig(mylist);
print(t)
'''

# 메뉴 고르기
'''
print("1. toast, 2. hamburer")
choice=int(input("1과 2 중에 선택하세요->"))

if choice==1:
    print("toast")
elif choice==2:
    print("hamberger")
'''
    
# 자판기 만들기
'''
print("〰"*8+"프친 푸드 가게"+"〰"*8)
print('1. 토스트(🍞) 1500원 2. 햄버거세트(🍔🍟🥤) 5300원 3. 피자(🍕) 9900원')

money = int(input("가진 금액>>"))
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

#랜덤 게임
'''
import random

d1=random.randint(1,6)
d2=random.randint(1,6)

if d1>d2:
    print('i win')
else:
    print('computer win')
'''

#랜덤 수 리스트 저장
'''
import random
dice=[ ]
for I in range(5):
    d=random.randint(1,6)
    dice.append(d)
print(dice)
'''

# 주사위 게임2
'''
import random
import time

def roll_dice(n):
    dice = [] # start with empty list of dice
    # add random numbers between 1 to 6 to the list
    for i in range(n):
        dice.append(random.randint(1,6))
    return dice

def find_winner(cdice_list, udice_list):
    computer_total = sum(cdice_list)
    user_total = sum(udice_list)
    print('Computer total', computer_total)
    print('User total',user_total )
    if user_total > computer_total:
        print('User wins')
    elif user_total < computer_total:
        print('Computer wins')
    else:
        print('It is a tie!')

def roll_again(choices, dice_list):
    print('Rolling again ...')
    time.sleep(3)
    for i in range(len(choices)):
        if choices[i] == 'r':
            dice_list[i] = random.randint(1,6)
    time.sleep(3)

def computer_strategy1(n):
    # create computer choices : roll everything again
    print('Computer is thinking ...')
    time.sleep(3)
    choices = '' # start with an empty list of choices
    for i in range(n):
        choices = choices + 'r'
    return choices

def computer_strategy2(n):
    # create computer choices: roll if < 5
    print('Computer is thinking ...')
    time.sleep(3)
    choices = '' # start with an empty list of choices
    for i in range(n):
        if computer_rolls[i] < 5:
            choices = choices + 'r'
        else:
            choices = choices + '-'
    return choices


# step1 in main program area - start game
number_dice = input('Enter number of dice:')
number_dice = int(number_dice)
ready = input('Ready to start? Hit any key to continue')

# step 2 in main program area - roll dice
# User turn to roll
user_rolls = roll_dice(number_dice)    # roll_dice 함수 호출
print('User first roll: ', user_rolls)

# step 4 - get user choices
user_choices = input("Enter - to hold or r to roll again : ")
# check length of user input
while len(user_choices) != number_dice:
    print('You must enter', number_dice, 'choices')
    user_choices = input("Enter - to hold or r to roll again : ")

# step 5 - roll again based on user choices
roll_again(user_choices, user_rolls)    # roll_again 함수 호출
print('Player new Roll: ', user_rolls)

# Computer's turn to roll
print('Computers turn ')
computer_rolls = roll_dice(number_dice)    # 함수 호출
print('Computer first roll: ', computer_rolls)

# step 6
# decide on what choice - using one of the strategy functions
computer_choices = computer_strategy2(number_dice)
print('Computer Choice: ', computer_choices)
# Computer rolls again using the choices it made
roll_again(computer_choices, computer_rolls)    # 함수 호출
print('Computer new Roll: ', computer_rolls)


# final line in code - deciding who wins
find_winner(computer_rolls,user_rolls)    # 함수 호출
'''


#문자, 숫자 대입
'''
age=5
#print("I'm %d years old", % age)
print("I'm %d years old" % age)


unit="years"
print("i'm 5 %s old" % unit)
'''


# 점수 비교
'''
score=68
if score<80:
    print('Fail')
else:
    print('Pass')
'''

#학점
'''
score=88
if score>=90:
    print('A')
elif score>=80:
    print('B')
elif score>=70:
    print('C')
else:
    print('Fail')    
'''


#학점
'''
score=[82, 74, 60, 12, 95]
n=0
for i in score:
    n+=1
    if i>=90:
        print(n, "번 A")
    elif i>=80:
        print(n, "번 B")
    elif i>=70:
        print(n, "번 C")
    elif i>=60:
        print(n, "번 D")
    else:
        print(n, "번 Fail")
'''


# continue문
'''
score=[82, 74, 30, 52, 95]
n=0
for i in score:
    n+=1
    if i<50:
        continue
    if n>4:
        break
    print(n,"번 50점 이상")
'''

# continue문
'''
i=0
while i<10:
    i+=1
    if i%2==1:
        continue
    print(i)
'''

# break문
'''
i=0
while i<=10:
    i+=1
    if i%2==0:
        print(i)
        if i==8:
            break
'''


#과속
'''
speed=85
limit=80
while speed>limit:
    print(speed, "과속, 감속하세요")
    speed-=1
    if speed<=limit:
        print(speed,"정상")
'''


# 숫자 오름차순 정렬
'''
agelist=[7, 3, 11, 22, 5, 9]
for i in range(0,6):
    min=agelist[i]
    minpos=i
    for j in range(i,6):
        if agelist[j]<=min:
            min=agelist[j]
            minpos=j
    min=agelist[minpos]; agelist[minpos]=agelist[i]; agelist[i]=min
print(agelist)    
'''

# 숫자 내림차순 정렬
'''
agelist=[7, 3, 11, 22, 5, 9]
for i in range(0,6):
    max=agelist[i]
    maxpos=i
    for j in range(i,6):
        if agelist[j]>=max:
            max=agelist[j]
            maxpos=j
    max=agelist[maxpos]; agelist[maxpos]=agelist[i]; agelist[i]=max     
print(agelist)
'''










