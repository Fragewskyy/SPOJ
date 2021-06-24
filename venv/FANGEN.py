import sys
while(True):
    n=int(input())
    if n < 0:
        L = []
        n = -n
        for i in range(n):
            print(((i) * '.') + ((n - i) * '*') + ((n - 1 - i) * '.') + ((i + 1) * '*'))
            L.append(((i) * '.') + ((n - i) * '*') + ((n - 1 - i) * '.') + ((i + 1) * '*'))
        for i in range(len(L) - 1, -1, -1):
            c = L[i]
            print(c[::-1])
        print()
    elif n > 0:
        L = []
        for i in range(n):
            print(((i + 1) * '*') + ((n - 1 - i) * '.') + ((n - i) * '*') + (i * '.'))
            L.append(((i + 1) * '*') + ((n - 1 - i) * '.') + ((n - i) * '*') + (i * '.'))
        for i in range(len(L) - 1, -1, -1):
            c = L[i]
            print(c[::-1])
        print()
    else:
        sys.exit(0)





