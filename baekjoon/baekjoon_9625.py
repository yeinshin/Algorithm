#https://www.acmicpc.net/problem/9625
#9625번-BABBA

a = [0]+[1]*44
b = [1]*45
k = int(input())

for n in range(2,k):
    a[n] = a[n-2]+a[n-1]
    b[n] = b[n-2]+b[n-1]

print(a[k-1],b[k-1])