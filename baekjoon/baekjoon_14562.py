#https://www.acmicpc.net/problem/14562
#14562번-태권왕
#S와 T가 같아지는 최소 연속 발차기 횟수를 구하기

for _ in range(int(input())):
    s,t = map(int,input().split())
    ans = int(1e9)
    def dfs(s,t,cnt):
        if s >= t:
            if s==t:
                global ans
                ans = min(ans,cnt)
            return
        dfs(s*2,t+3,cnt+1)
        dfs(s+1,t,cnt+1)
    dfs(s,t,0)
    print(ans)