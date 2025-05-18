r = int(input())
for i in range(0,r):
    for j in range(0,r-i-1):
        print(" ",end="")
    for k in range(0,i+1):
        print("* " ,end="")
    print()
for i in range(0,r-1):
    for j in  range(0,i+1):
        print(" ",end="")
    for k in range(0,r-i-1):
        print("* ",end="")
    print()