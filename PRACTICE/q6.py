a = input()
v = 0
c = 0
d = 0
for i in a:
    if i.isdigit():
        d += 1
    elif i.isalpha():
        if i in "aeiouAEIOU":
            v += 1
        else:
            c += 1    
    
    
print(f"Number of Vowels: {v}")
print(f"Number of Consonants: {c}")
print(f"Number of Digits: {d}")
