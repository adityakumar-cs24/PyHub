a,b,c = input().split()
a = int(a)
b = int(b)
if b!=0:
    if c == "+":
        print(a+b)
    elif c == "-":
        print(a-b)
    elif c == "*":
        print(a*b)
    elif c == "/":
        print(a/b)
    else:
        print("Invalid Operator")
else:
    print("Division by zero is not allowed.")