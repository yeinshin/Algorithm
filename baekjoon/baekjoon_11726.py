#https://www.acmicpc.net/problem/11726
#11726번-2×n 타일링

#첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
n=int(input())
d=[1,2]+[0]*(n-2)
if n<=2:
    print(d[n-1])
else:
    for i in range(2,n):
        d[i]=d[i-1]+d[i-2]
    print(d[n-1]%10007)