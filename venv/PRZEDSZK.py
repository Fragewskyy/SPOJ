def nwd(a,b):
    if b>0:
        return nwd(b, a%b)
    return a

n=int(input())

for i in range(n):
    a,b=map(int, input().split())
    print(int((a*b)/nwd(a,b)))
