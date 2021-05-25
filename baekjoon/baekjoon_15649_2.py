#https://www.acmicpc.net/problem/15649
#15649번-N과 M (1)
#recursion을 이용한 풀이

n,m = map(int,input().split())
visited = [False]*(n+1)
permu=list()

def recursion(cnt,permu):
    
    if cnt==m:
        for p in permu:
            print(p,end=' ')
        
        print()
        return
    
    for i in range(1,n+1):
        if not visited[i]:
            permu.append(i)
            visited[i]=True
            recursion(cnt+1,permu) 
            permu.pop()
            visited[i]=False
            # print(permu,'cnt:',cnt)

recursion(0,permu)
