n=int(input())

for i in range(n):
    a=int(input())
    xd=0
    L=input().split()
    for e in range(len(L)):
        xd+=int(L[e])
    print(xd)