n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(65,65+2*i-1):
        print(chr(j), end=" ")
    print()