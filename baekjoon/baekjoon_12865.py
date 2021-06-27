#https://www.acmicpc.net/problem/12865
#12865번-평범한 배낭 / 풀이 살짝 참고

#n: 물품의 수, k: 준서가 버틸 수 있는 무게
n,k = map(int,input().split())
w = [] #물건의 무게
v = [] #물건의 가치
for _ in range(n):
    a,b = map(int,input().split())
    w.append(a)
    v.append(b)

dp = [0]*(k+1)

for j in range(n):
    for i in range(k,0,-1):
        if i>=w[j]:
            dp[i] = max(dp[i-w[j]]+v[j],dp[i])

print(dp[-1])
