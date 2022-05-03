#https://www.acmicpc.net/problem/15918
#15918번-랭퍼든 수열쟁이야!!
import sys
input = sys.stdin.readline
n,x,y = map(int,input().split())
nums = list(range(1,n+1))
used = [1]*(n+1)
ans = 0
result = [0]*(2*n+1)
result[x] = y-x-1
result[y] = y-x-1
used[y-x-1] = 0

def backtracking(n,idx):
    global ans

    if idx==2*n:
        ans+=1
        return

    if result[idx]!=0:
        backtracking(n,idx+1)
    else:
        for i in range(1,n+1):
            if used[i]==1 and idx+i+1<=2*n and result[idx+i+1]==0:
                used[i]=0
                result[idx]=i
                result[idx+i+1]=i
                backtracking(n,idx+1)
                used[i]=1
                result[idx]=0
                result[idx+i+1]=0

backtracking(n,1)
print(ans)