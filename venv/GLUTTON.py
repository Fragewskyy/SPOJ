a=int(input())
for i in range(a):
    n,m = map(int, input().split())
    cakeSum=0
    wynik=0
    for j in range(n):
        k=int(input())
        cakesAmount = 86400//k
        cakeSum+=cakesAmount
    if cakeSum%m != 0:
        wynik = (cakeSum//m)+1
    else:
        wynik = cakeSum//m
    print(wynik)
