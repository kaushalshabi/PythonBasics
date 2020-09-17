import emp, pickle
f = open("emp.dat", "wb")
n = int(input("Enter The number of Employees:"))
for i in range(n):
    eno = int(input("Enter Employee Number:"))
    ename = input("Enter Employee Name:")
    esal = float(input("Enter Employee Salary:"))
    eaddr = input("Enter Employee Address:")
    e = emp.Employee(eno, ename, esal, eaddr)
    pickle.dump(e, f)
print("Employee Objects pickled successfully")