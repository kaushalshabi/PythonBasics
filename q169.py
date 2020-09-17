def decor(func):
    def inner(name):
        if name=="Sunny":
            print("Hello Sunny Bad Morning")
        else:
            func(name)
    return inner
def wish(name):
    print("Hello",name,"Good Morning")
decorfunction=decor(wish)
wish("Durga") #decorator wont be executed
wish("Sunny") #decorator wont be executed
decorfunction("Durga")#decorator will be executed
decorfunction("Sunny")#decorator will be executed