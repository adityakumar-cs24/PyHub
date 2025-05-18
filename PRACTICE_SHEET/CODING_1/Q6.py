a,b,c = map(int,input("Enter 3 no.:- ").split())
if(a > b and a > c):
    print(f"{a} is greater.")
elif(b > c):
    print(f"{b} is greater.")
else:
    print(f"{c} is greater.")