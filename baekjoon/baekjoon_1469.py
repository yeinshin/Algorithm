#https://www.acmicpc.net/problem/1469
#1469번-숌 사이 수열
import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(map(int,input().split()))
used = [1]*n
ans = [-1]*(n*2)

def backtracking(depth):
    if depth==2*n:
        print(' '.join(map(str,ans)))
        sys.exit(0)

    if ans[depth]!=-1:
        backtracking(depth+1)
    else:
        for i in range(n):
            if used[i]==1 and depth+nums[i]+1<2*n and ans[depth+nums[i]+1]==-1:
                ans[depth],ans[depth+nums[i]+1] = nums[i],nums[i]
                used[i]=0
                backtracking(depth+1)
                used[i]=1
                ans[depth],ans[depth+nums[i]+1] = -1,-1

backtracking(0)
print(-1)