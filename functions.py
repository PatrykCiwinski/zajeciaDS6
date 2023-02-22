def fun(thing):
    if type(thing) in [tuple,list,bytes,str]:
        print("Wprowadzony parametr jest obiektem iterowalnym")
    elif type(thing) in [complex,float,int]:
        print("Wprowadzony parametr jest typu liczbowego")


fun(1)

