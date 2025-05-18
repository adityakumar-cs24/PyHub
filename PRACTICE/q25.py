scores = eval(input().replace("scores = ",""))
l = len(scores)
avg = 0
for score in scores:
    avg = avg + score / l
print(f"{avg:.2f}")