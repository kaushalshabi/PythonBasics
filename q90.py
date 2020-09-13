s=input("Enter Some String:")
l=[]
for x in s:
    if x not in l:
        l.append(x)
output=''.join(l)
print(output)