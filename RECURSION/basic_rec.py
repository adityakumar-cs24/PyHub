n = int(input())
def show(n):
    if(n == 10):
        return
    print(n)
    show(n+1)
show(n)