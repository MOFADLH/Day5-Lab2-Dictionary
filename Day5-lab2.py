from array import *

numbers = [["Amal","1111111111"],["Mohammed","2222222222"],["Khadijah","3333333333"],["Abdullah","4444444444"],["Rawan","5555555555"],["Faisal","6666666666"],["Layla","7777777777"]]
found= "Sorry, the number is not found"
n = input("Enter the number:")
len=len(n)
for i in n: 
    if not(i.isdigit()) or len!=10:
        found="This is invalid number"
else:
    for y in range(6):
        if numbers[y][1]== n:
            found=numbers[y][0]
print(found)