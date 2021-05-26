#https://www.acmicpc.net/problem/2529
#2529번-부등호
#각 부등호의 앞뒤에 들어가는 숫자는 { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }중에서 선택해야 하며 선택된 숫자는 모두 달라야 한다. 
#제시된 k개의 부등호 순서를 만족하는 (k+1)자리의 정수 중에서 최댓값과 최솟값을 찾아야 한다. 
#k의 범위는 2 ≤ k ≤ 9 이다.

import sys
input = sys.stdin.readline

k=int(input())
array = list(input().split())
visited = []
INF = int(1e9)
max_result = '0'*(k+1)
min_result = '9'*(k+1)

def dfs(start,cnt):
    global max_result,min_result

    if cnt==(k):
        max_result=max(max_result,''.join(visited))
        min_result=min(min_result,''.join(visited))
        return

    for j in range(10):
        if array[cnt]=='>':
            if start>j and str(j) not in visited:
                visited.append(str(j))
                dfs(j,cnt+1)
                visited.pop()

        #if array[cnt]=='<'
        else: 
            if start<j and str(j) not in visited:
                visited.append(str(j))
                dfs(j,cnt+1)
                visited.pop()

for i in range(10):
    visited.append(str(i))
    dfs(i,0)
    visited.pop()

print(max_result)
print(min_result)