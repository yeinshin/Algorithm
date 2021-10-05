#https://www.acmicpc.net/problem/10870
#10870번-피보나치 수 5
a = [0]*21
a[1]=1
n = int(input())
if 0<=n<=1: print(a[n])
else:
    for i in range(2,n+1):
        a[i]=a[i-1]+a[i-2]
    print(a[n])

