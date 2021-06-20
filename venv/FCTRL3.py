n=int(input())


for i in range (n):
    a=input()
    s=1
    if int(a)<=9:
        for e in range(1, int(a) + 1):
            s *= e
        s = s % 100
        d = int(s / 10)
        print(d, int(s - 10 * d))
    else:
        print(0, 0)


