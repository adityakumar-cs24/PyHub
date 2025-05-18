char = input("Enter a character : ")
if (char >= 'A' and char <= 'Z') or (char >= 'a' and char <='z') :
    print(f"{char} is alphabet.")
elif (char >= '1' and char <= '9') :
    print(f"{char} is digit.")
else :
    print(f"{char} is special character.")