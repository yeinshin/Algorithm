#https://www.acmicpc.net/problem/9461
#9461번-파도반 수열

for _ in range(int(input())):
    n = int(input())
    p=[1,1,1]
    if n<=3:
        print(p[n-1])
    else:
        for i in range(3,n):
            p.append(p[i-2]+p[i-3])
        print(p[n-1])