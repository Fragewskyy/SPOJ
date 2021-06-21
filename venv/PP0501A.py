def nwd(a,b):
    if b>0:
        return nwd(b, a%b)
    return a

n=int(input())

for i in range(n):
    x,d = map(int, input().split())
    print(nwd(x,d))