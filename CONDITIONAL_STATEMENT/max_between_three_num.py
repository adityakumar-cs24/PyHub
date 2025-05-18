num1 = int(input("Enter 1st no. : "))
num2 = int(input("Enter 2nd no. : "))
num3 = int(input("Enter 3rd no. : "))
if num1 > num2 and num1 > num3 :
    print(f"{num1} is greater.")
elif num2 > num3 :
    print(f"{num2} is greater.")
else :
    print(f"{num3} is greater.")
