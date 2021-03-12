
# 숫자를 입력받아 홀수인지 짝수인지 구별
'''
c=int(input())
if c%2==0:
    print('c는 짝수이다.')
else:
    print('c는 홀수이다.')
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
    x-=100
while x>=10:
    m10+=1
    x-=10
while x>=1:
    m1+=1
    x-=1
print(m100, m10, m1)    
'''



#나이가 (17, 14, 18, 13, 19) 인 사람들이 있는데 나이가 13인 사람이 있는가?
'''
agelist=[17, 14, 18, 13, 19]
ans='no'
for i in range(0,5):
    agelist[i]==13
    ans='yes'
print(ans)
'''

#나이가 (17, 14, 18, 13, 19) 인 사람들이 있는데 가장 나이가 많은 값 얼마인가?
'''
agelist=[17, 14, 18, 13, 19]
max=0
for i in range(0,5):
    if agelist[i]>max:
        max=agelist[i]
print(max)
'''

#나이가 (17, 14, 18, 13, 19) 인 사람들이 있는데 나이순으로 알려다오.   #################
'''
agelist=[17, 14, 18, 13, 19]
for i in range(0,5):
    min=agelist[i]   # 17, 14, 18, 13, 19
    minpos=i     ###0, 1, 2, 3, 4
    for j in range(i,5):
        if min>=agelist[j]:
            min=agelist[j]   #17, 14, 13
            minpos=j     ###0, 1, 3
    min=agelist[minpos]; agelist[minpos]=agelist[i]; agelist[i]=min       ###     
print(agelist)
'''

'''
agelist=[17, 14, 18, 13, 19]
for k in range(0,5):
    min=agelist[k]
    minpos=k
    #print(min)
    #print(minpos)
    for j in range(k,5):
        if agelist[j]<=min:
            min=agelist[j]
            minpos=j
            #print(min)
            #print(minpos)
    min=agelist[minpos]; agelist[minpos]=agelist[k]; agelist[k]=min
print(agelist)
'''
#
'''
agelist=[17, 14, 18, 13, 19]
agelist.sort()
print(agelist)
'''

# 리스트 원소에서 10 찾기
'''
mylist=[3,7,2,10,6]
ans='10은 없다'
for i in range(0,5):
    if mylist[i]==10:
        ans='10 찾았다'
print(ans)
'''


# 리스트에서 가장 큰 원소 찾기
'''
mylist=[3,7,15,10,6]
max=0
for i in range(0,5):
    if mylist[i]>max:
        max=mylist[i]
print(max)
'''



######### 나이가 (17, 14, 18, 13, 19) 인 사람들이 있는데 나이순으로 알려다오. 


agelist=[17, 14, 18, 13, 19]
for i in range(0,5):
    min=agelist[i]
    minpos=i
    for j in range(i,5):
        if min>=agelist[j]:
            min=agelist[j]
            minpos=j
    min=agelist[minpos]; agelist[minpos]=agelist[i]; agelist[i]=min   # 왜 minpos인거지??????????
print(agelist)    

'''
agelist=[17, 14, 18, 13, 19]
for i in range(0,5):
    min=agelist[i]   # 17, 14, 18, 13, 19
    minpos=i     ###0, 1, 2, 3, 4
    for j in range(i,5):
        if min>=agelist[j]:
            min=agelist[j]   #17, 14, 13
            minpos=j     ###0, 1, 3
    min=agelist[minpos]; agelist[minpos]=agelist[i]; agelist[i]=min       ###     
print(agelist)
'''










