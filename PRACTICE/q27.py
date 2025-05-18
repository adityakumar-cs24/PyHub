employees = eval(input().replace("employees = ",""))
find = input().replace("find = ","")
if find in employees:
   print(f"Index of '{find}': {employees.index(find)}")
else:
    print("-1")