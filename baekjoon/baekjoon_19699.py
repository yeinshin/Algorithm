#https://www.acmicpc.net/problem/19699
#19699번-소-난다!
n,m = map(int,input().split())
cows = list(map(int,input().split()))
result = set()

def checkprime(cow):
    for i in range(2,cow):
        if cow%i==0: return False
    return True

def dfs(cnt,check,kg):
    if cnt==m: 
        if checkprime(kg):
            result.add(kg)
        return
    for i in range(n):
        if i not in check:
            dfs(cnt+1,check+[i],kg+cows[i])

dfs(0,[],0)
if result: print(*sorted(result),sep=' ')
else: print(-1)