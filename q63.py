s = input("Enter Some String:")
i = 0
for x in s:
    print("The character present at positive index {} and at nEgative index {}  is {}".format(i, i - len(s), x))
    i = i + 1