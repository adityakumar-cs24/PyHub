n = map(int,input().split())
res = ""
for i in n:
    if 1 <= i <= 26:
        res += chr(i+64)
    elif 27 <= i <= 52:
        res += chr(i+70)
print(res)  