my_list, target = eval(input().replace("nums = ", "").replace("target = ", ""))
for i in range(len(my_list)):
    for j in range(i+1,len(my_list)):
        if my_list[i] + my_list[j] == target:
            print([i,j])
            exit()
print("No valid pair found.")
