ms1 = int(input("Enter marks of 1st subject: "))
ms2 = int(input("Enter marks of 2nd subject: "))
ms3 = int(input("Enter marks of 3rd subject: "))
ms4 = int(input("Enter marks of 4th subject: "))
ms5 = int(input("Enter marks of 5th subject: "))
total_marks = ms1 + ms2 + ms3 + ms4 + ms5
average_marks = (ms1 + ms2 + ms3 + ms4 + ms5)/5
percentage = (total_marks/500)*100
print(f"Total marks : {total_marks}")
print(f"Average marks : {average_marks}")
print(f"Percentage : {percentage:.2f} %")