def wish(name):
    print("Good Morning:", name)


greeting = wish
greeting('Durga')
wish('Durga')
del wish
 # wish('Durga')   ==>NameError: name 'wish' is not defined
greeting('Pavan')