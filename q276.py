class Student:
    ''''' This is student class with required data'''
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z
    def display(self):
        print("Student Name:{}\nRollno:{} \nMarks:{}".format(self.name,self.rollno,self.marks) )
s1=Student("Durga",101,80)
s1.display()
s2=Student("Sunny",102,100)
s2.display()
