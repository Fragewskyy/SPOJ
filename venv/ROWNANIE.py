a=float()
b=float()
c=float()


while(a,b,c = map(float, input().split())):
    a,b,c = map(float, input().split())
    delta=((b*b)-(4*a*c))
    if delta>0:
        print('2')
    elif delta==0:
        print('1')
    elif delta<0:
        print('0')