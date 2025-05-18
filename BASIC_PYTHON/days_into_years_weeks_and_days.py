days = int(input("Enter Days : "))
year = days//365
week = (days%365) // 7
remaining_days = days - ((year * 365) + (week * 7)) 
print(f"Year : {year}")
print(f"Week : {week}")
print(f"Remaining days : {remaining_days}")