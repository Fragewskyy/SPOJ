s=int(input())
for i in range(s):
    finalList = []
    n, x, y = map(int, input().split())
    for k in range(n):
        if k%x==0 and k%y!=0:
            finalList.append(k)
    print(*finalList)