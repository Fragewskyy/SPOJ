n=int(input())
for i in range(n):
    k=0
    a=input()
    s=a
    while a!=a[::-1]:
        s=int(a)+int(a[::-1])
        a=str(s)
        k+=1
    print(s,k)