n = int(input("Enter a number:"))
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(n + 1 - j, end=" ")
    print()