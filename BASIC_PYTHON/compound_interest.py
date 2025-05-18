Principal = float(input("Enter Principal amount : "))
Rate = float(input("Enter rate : "))
Time = float(input("Enter time : "))
CI = Principal * (1 + Rate/100) ** Time
print(f"Compound Interest is : {CI:.2f}")