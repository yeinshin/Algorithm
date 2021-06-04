#https://www.acmicpc.net/problem/14470
#14470번-전자레인지

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
answer = 0 

while a!=b:
    if a<0:
        answer+=c
        a+=1
    elif a==0:
        answer=d+e+answer
        a+=1
    else:
        answer+=e
        a+=1
    
print(answer)

