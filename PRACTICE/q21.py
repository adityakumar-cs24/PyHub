my_list = eval(input()) 
my_list.sort()
miss = my_list[0]
for i in range(1,len(my_list)):
    if miss+1 != my_list[i]:
        print(miss+1)
        break
    miss = my_list[i]
