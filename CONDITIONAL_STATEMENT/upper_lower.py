char = input("Enter a character : ")
if (char >= 'A' and char <= 'Z') :
    print(f"{char} is upper case alphabet.")
elif (char >= 'a' and char <='z') :
    print(f"{char} is lower case alphabet.")
else :
    print(f"{char} is not alphabet.")