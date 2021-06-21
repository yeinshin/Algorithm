#https://www.acmicpc.net/problem/10826
#10826번-피보나치 수 4

n = int(input())
p = [0]*n
if n<=1:
    print(n)
else:
    p=[0]*(n+1)
    p[1]=1
    p[2]=1
    for i in range(3,n+1):
        p[i]=p[i-2]+p[i-1]
    print(p[n])