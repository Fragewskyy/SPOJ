n=int(input())
def isPrime(a):
    if a<2:
        return False
    else:
        for i in range(2,a):
            if a%i==0:
                return False
    return True

for i in range(n):
    a=int(input())
    if isPrime(a)==True:
        print("TAK")
    else:
        print("NIE")