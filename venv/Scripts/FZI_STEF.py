def add(L, beg, end):
    result=0
    for i in range(beg,end+1):
        result+=L[i]
    return result;

max=0
n=int(input())
L=[]

for i in range(n):
    a=int(input())
    L.append(a)



for i in range(n):
    s=i
    for s in range(n):
        result=add(L, i, s)
        if result>max:
            max=result

print(max)

