R = []
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += str(ele)
    return str1

def perm(n, p = 0):
    if len(n) == p:
        n=list(map(int, n))
        R.append(listToString(n))
    else:
        for i in range(p, len(n)):
            n[i], n[p] = n[p], n[i]
            perm(n, p + 1)
            n[i], n[p] = n[p], n[i]

def is_prime(n):
    if n == 1:
        return False
    factors = 0
    for i in range(1, n+1):
        if n % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False

L = list(map(int, input().split()))
perm(L)

counter = 0

for i in range(len(R)):
    if is_prime(int(R[i])) == True:
        counter+=1

print(counter)

