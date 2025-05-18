a = input()
try:
    int(a)
    print("Int")
except ValueError:  
    try:
        float(a)
        print("float")
    except ValueError:
        print("Str")
