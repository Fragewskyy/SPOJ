n=int(input())
# for i in range(n):
#     newstr=""
#     S=[]
#     s=input();
#     for i in range(len(s)):
#         S.append(s[i])
#     S=set(S)
#     S=list(S)
#     for i in range(len(S)):
#         s.count(S[i])
#         if s.count(S[i])>2:
#             newstr += S[i]+str(s.count(S[i]))
#         elif s.count(S[i])==2:
#             newstr += 2*S[i]
#         elif s.count(S[i])==1:
#             newstr += S[i]
#     print(newstr)
for i in range(n):
    s=input()
    newstr=""
    S=[]
    for i in range(len(s)):
        S.append(s[i])
    S=set(S)
    S=list(S)
    for i in range(len(S)):
        aktualny_znak=S[i]
        s.count(aktualny_znak)
        if s.count(aktualny_znak)>2:
            newstr+= aktualny_znak + str(s.count(aktualny_znak))
        elif s.count(aktualny_znak)==2:
            newstr+=2*aktualny_znak
        elif s.count(aktualny_znak) == 1:
            newstr+=aktualny_znak
        s = s.replace(aktualny_znak, "")

    print(newstr)
