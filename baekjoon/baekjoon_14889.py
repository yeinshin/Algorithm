#https://www.acmicpc.net/problem/14889
#14889번-스타트와 링크
import sys
input = sys.stdin.readline
N = int(input())
startlink = [list(map(int,input().split())) for _ in range(N)]
selected = [0]*(N//2)
ans = int(1e9)
visited = [False]*N
def combi(n,cnt,now):
    global ans
    if cnt == n//2:
        unselected = []
        sumA = 0
        sumB = 0
        for x in range(n):
            if not visited[x]: unselected.append(x)
        for x in range(n//2):
            for y in range(n//2):
                if x!=y: 
                    sumA+=startlink[selected[x]][selected[y]]
                    sumB+=startlink[unselected[x]][unselected[y]]      
        ans = min(ans,abs(sumA-sumB))
        return
    
    for i in range(now,n):
        selected[cnt] = i
        visited[i] = True
        combi(n,cnt+1,i+1)
        visited[i] = False

combi(N,0,0)
print(ans)