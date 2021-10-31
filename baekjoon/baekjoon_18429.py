#https://www.acmicpc.net/problem/18429
#18429번-근손실

n,k = map(int,input().split())
kit = list(map(int,input().split()))
result = 0
def dfs(cnt,before,now):
    global result
    if cnt==n:
        result+=1
        return
    
    for i in range(n):
        if i not in before and now-k+kit[i]>=500:
            dfs(cnt+1,before+[i],now-k+kit[i])
dfs(0,[],500)
print(result)
