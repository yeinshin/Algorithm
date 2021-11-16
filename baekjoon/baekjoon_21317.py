#https://www.acmicpc.net/problem/21317
#21317번-징검다리 건너기

n = int(input())
r = [list(map(int,input().split())) for _ in range(n-1)]
k = int(input())
ans = int(1e9)
def dfs(energy,check,cnt):
    
    if cnt==n-1:
        global ans
        ans = min(ans,energy)
        return

    for i in range(1,4):
        if cnt+i<=n-1:
            if i==1:dfs(energy+r[cnt][0],check,cnt+i)
            elif i==2 and cnt+2<=n:dfs(energy+r[cnt][1],check,cnt+i)
            elif i==3 and check:dfs(energy+k,False,cnt+i)
dfs(0,True,0)
print(ans)