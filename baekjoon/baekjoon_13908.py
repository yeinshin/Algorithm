#https://www.acmicpc.net/problem/13908
#13908번-비밀번호
n,m = map(int,input().split())
result = 0
if m!=0: k = list(map(int,input().split()))
else: k=[]
def dfs(cnt,now,pw):
    global result
    if cnt==n:
        for j in k:
            if j not in pw: break
        else: result+=1
        return
    for i in range(10):
        dfs(cnt+1,i,pw+[i])
dfs(0,-1,[])
print(result)