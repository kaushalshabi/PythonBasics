s=input("Enter any character:")
if s.isalnum():
    print("Alpha Numeric Character")
if s.isalpha():
    print("Alphabet character")
if s.islower():
    print("Lower case alphabet character")
else:
    print("Upper case alphabet character")
else:
    print("it is a digit")
elif s.isspace():
    print("It is space character")
else:
    print("Non Space Special Character")