
#1
for num in range(10, 14):
    for i in range(2, num):
        if num%i == 1:
            print(num)
            break

#2
valueOne = 5 ** 2
valueTwo = 5 ** 3
print(valueOne+valueTwo)

#3
x = 0
a = 0
b = -5
if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

#4 ??????????
var= "James Bond"
print(var[2::-1])

#5
x = 36 / 4 * (3 + 2) * 4 + 2
print(x)

#6 ??????????
a, b = 12, 5
if a + b:
    print('True')
else:
    print('False')

#7 에러
sampleList = ["Jon", "Kelly", "Jessa"]
sampleList.append(2, "Scott")
print(sampleList)

#8 에러
var1 = 1
var2 = 2
var3 = "3"
print(var + var2 + var3)

#9 ????????
listOne = [20, 40, 60, 80]
listTwo = [20, 40, 60, 80]
print(listOne == listTwo)

listOne = [20, 40, 60, 80]
listTwo = [20, 40, 60, 80]
print(listOne == listTwo)
print(listOne is listTwo)

#10
str = "pynative"
print (str[1:3])



