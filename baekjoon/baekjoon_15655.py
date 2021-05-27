#https://www.acmicpc.net/problem/15655
#15655번-N과 M(6)
#입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

n,m = map(int,input().split())
array = sorted(list(map(int,input().split())))
visited = list()

def dfs(cnt,now):
    if cnt == m:
        print(*visited)
        return
    
    for a in array:
        if now<a and a not in visited:
            visited.append(a)
            dfs(cnt+1,a)
            visited.pop()

dfs(0,0)