#https://www.acmicpc.net/problem/15650
#15650번-N과 M(2)
#recursion을 이용한 풀이

n,m = map(int,input().split())
visited = [False]*(n+1)
permu=list()

def recursion(cnt,permu,k):
    
    if cnt==m:
        for p in permu:
            print(p,end=' ')
        
        print()
        return

    for i in range(1,n+1):
        if not visited[i] and k<=i:
            k=i
            permu.append(i)
            visited[i]=True
            recursion(cnt+1,permu,k) 
            permu.pop()
            visited[i]=False

recursion(0,permu,1)
