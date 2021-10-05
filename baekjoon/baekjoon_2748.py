#https://www.acmicpc.net/problem/2748
#2748번-피보나치 수 2
n = int(input())
a = [0]*(n+1)
a[1]=1
if 0<=n<=1: print(a[n])
else:
    for i in range(2,n+1):
        a[i]=a[i-1]+a[i-2]
    print(a[n])