#2468번-안전 영역

import sys
import copy

input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())

graph = [[int(i) for i in input().split()] for _ in range(n)]

def dfs(x,y,h,test):


    if 0>x or 0>y or x>=n or y>=n:
        return -1

    if test[x][y]>h:
        
        test[x][y]=0

        dfs(x-1,y,h,test)
        dfs(x+1,y,h,test)
        dfs(x,y-1,h,test)
        dfs(x,y+1,h,test)

        return 1
    
    return -1

result = list()

end = max(map(max, graph))

for h in range(end):
    cnt=0
    test = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if test[i][j]>h:
                if dfs(i,j,h,test) == 1:
                    cnt+=1
    
    result.append(cnt)

# print(result,end='\n\n')
print(max(result))