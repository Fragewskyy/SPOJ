k, n = map(int, input().split())

L = []
R = []
for i in range(k):
    L.append(i)

base = (n - sum(L)) / k

for i in range(k):
    R.append(int(base + L[i]))

print(*R)
