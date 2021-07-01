import sys

L = []
try:
    while (True):
        n = input()
        if n == '+':
            k = int(input())
            if k in L:
                print(':(')
            else:
                L.append(k)
                print(':)')
        elif n == '-':
            if len(L) > 0:
                print(L[len(L) - 1])
                L.pop(len(L) - 1)
            elif len(L) == 0:
                print(':(')

except EOFError:
    sys.exit(0)
