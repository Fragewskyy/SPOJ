n=int(input())

for i in range(n):
    L=input().split()
    a=int(L[0])
    b=int(L[1])
    ostA=str(a)

    k=int(ostA[len(ostA)-1])**b
    s=str(k)
    print(s[len(s)-1])