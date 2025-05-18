str1,str2 = input().split('" "')
str1 = str1.strip('"')
str2 = str2.strip('"')  
count = 0
for i in range(len(str1) - len(str2) + 1):
    if str1[i:i + len(str2)] == str2:
        count += 1
print(count)