#https://www.acmicpc.net/problem/15651
#15651번-N과 M(3)
#recursion을 이용한 풀이

n,m = map(int,input().split())
permu=list()

def recursion(cnt,permu):
    
    if cnt==m:
        for p in permu:
            print(p,end=' ')
        
        print()
        return
    
    for i in range(1,n+1):
        permu.append(i)
        recursion(cnt+1,permu) 
        permu.pop()

recursion(0,permu)