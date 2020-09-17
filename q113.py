num1=[10,20,30,40]
num2=[30,40,50,60]
num3=[ i for i in num1 if i not in num2]
print(num3)
num4=[i for i in num1 if i in num2]
print(num4)