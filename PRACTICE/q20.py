my_list = eval(input())
my_list = list(set(my_list))
my_list.sort()
if len(my_list) > 1:
    if my_list[-1] != my_list[-2]:
        print(my_list[-2])
    else:
        print("No second highest score.")
else:
    print("No second highest score.")