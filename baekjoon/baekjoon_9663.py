#https://www.acmicpc.net/problem/9663
#9663번-N-Queen

n= int(input())
answer = 0
column,d1,d2=list(),list(),list()

def dfs(n,x):
    global answer

    if x==n:
        answer+=1
        return
    
    for y in range(n):
        if y not in column and (x+y) not in d1 and (x-y) not in d2:
            column.append(y)
            d1.append(x+y)
            d2.append(x-y)
            dfs(n,x+1)
            column.pop()
            d1.pop()
            d2.pop()

dfs(n,0)
print(answer)