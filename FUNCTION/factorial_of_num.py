a = int(input())
def cal_fact(a):
    fact = 1
    for i in range(1,a+1):
        fact *= i
    print(fact)
cal_fact(a)