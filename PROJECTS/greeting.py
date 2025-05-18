import time
t = time.strftime('%H:%M:%S')
print(t)
H = int(time.strftime('%H'))
if(H>0 and H<12):
    print("GOOD MORNING!!")
elif(H>=12 and H<17):
    print("GOOD AFTERNOON!!")
elif(H>=17 and H<=0):
    print("GOOD NIGHT!!") 