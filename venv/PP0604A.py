n=int(input())
for i in range(n):
    L=input().split()
    for i in range(len(L)):
        L[i]=int(L[i])
    print(sum(L)/len(L))