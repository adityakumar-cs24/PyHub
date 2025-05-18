words,pref = eval(input().replace("words = ","").replace("pref = ",""))
count = 0
for word in words:
    if word.startswith(pref):
        count += 1
print(count)