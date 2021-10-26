#https://www.acmicpc.net/problem/2435
#2435번-기상청 인턴 신현수
n,k = map(int,input().split())
ondo = list(map(int,input().split()))
result = -int(1e9)
for i in range(n-k+1):
    cnt = 0
    for j in range(i,k+i):
        cnt+=ondo[j]
    result = max(result,cnt)
print(result)
    
