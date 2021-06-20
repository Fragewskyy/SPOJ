n=int(input())
for i in range(n):
    p=input()
    test=int(p[0])+3*int(p[1])+7*int(p[2])+9*int(p[3])+int(p[4])+3*int(p[5])+7*int(p[6])+9*int(p[7])+int(p[8])+3*int(p[9])+int(p[10])
    if test%10==0:
        print('D')
    else:
        print('N')