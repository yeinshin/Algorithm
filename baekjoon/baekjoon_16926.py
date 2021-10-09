#https://www.acmicpc.net/problem/16926
#16926번-배열 돌리기1(풀이참고)
n,m,r = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n,m)//2):
        s_x,s_y = i,i
        now = array[i][i]
        for j in range(i+1,n-i):
            s_x=j
            temp = array[s_x][s_y]
            array[s_x][s_y]=now
            now = temp
        for j in range(i+1,m-i):
            s_y=j
            temp = array[s_x][s_y]
            array[s_x][s_y]=now
            now = temp
        for j in range(i+1,n-i):
            s_x = n - j - 1
            temp=array[s_x][s_y]
            array[s_x][s_y]=now
            now=temp
        for j in range(i+1,m-i):
            s_y = m - j - 1
            temp=array[s_x][s_y]
            array[s_x][s_y]=now
            now=temp 

for i in range(n):
    print(*array[i],sep=' ')