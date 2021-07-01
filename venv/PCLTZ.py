def solve(c):
    p = 0
    while True:
        if c != 1:
            if c % 2 == 1:
                p += 1
                c = 3 * c + 1
            elif c % 2 == 0:
                p += 1
                c = c / 2
        else:
            return p


n = int(input())
for i in range(n):
    k = int(input())
    print(solve(k))
