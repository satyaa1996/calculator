print ("Thanks for Using our Calculator")
a = input("enter no.")
a = int(a)
sign = input ("enter operator")
b = input("enter no.")
b = int(b)
def var (a,sign,b) :
    if sign  == "-" :
        print (a - b)
    if sign == "+" :
        print (a + b)
    if sign == "*" :
        print(a * b)
    if sign == "/" :
        print (a / b)

var(a,sign,b)
