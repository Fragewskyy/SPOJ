a=input()
b=input()
c=input()

s=int()

for i in range(len(a)):
    if a[i]!=b[i] or a[i]!=c[i]:
        if c[i]==b[i]:
            s+=2
        else:
            s+=1

print(s)