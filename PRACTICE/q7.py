a,b,c = input().split()
a = int(a)
c = int(c)
if c!=0:
    if b == "+":
        print(a+c)
    elif b == "-":
        print(a-c)
    elif b == "*":
        print(a*c)
    elif b == "/":
        print(a/c)
    else:
        print("Invalid Operator")
else:
    print("Division by zero is not allowed.")