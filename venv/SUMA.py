import sys
sum=0
while(True):
    try:
        n = int(input())
        sum += n
        print(sum)
    except EOFError:
        sys.exit(0)
