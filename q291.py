class Test:
    x = 10
    def __init__(self):
        self.y = 20

    def m1(self):
        self.x = 888
        self.y = 999
t1 = Test()
t2 = Test()
t1.m1()
print(t1.x, t1.y)
print(t2.x, t2.y)   