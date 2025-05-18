a1,a2,a3 = map(int,input("Enter 3 angles.:- ").split())
if(a1 + a2 + a3 != 180):
    print("Invalid Triangle!")
else:
    if(a1 == 90 or a2 == 90 or a3 == 90):
        print("Right Triangle.")
    elif(a1 > 90 or a2 > 90 or a3 > 90):
        print("Obtuse Triangle.")
    else:
        print("Acute Triangle.")