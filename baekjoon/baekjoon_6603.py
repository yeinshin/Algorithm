#https://www.acmicpc.net/problem/6603
#6603번-로또

def dfs(cnt,arr,comb):

    if cnt == 6:
        print(*comb)
        return

    for i in range(len(arr)):
        if not visited[arr[i]]:
            visited[arr[i]]=True
            comb.append(arr[i])

            dfs(cnt+1,arr,comb)

            comb.pop()

            for j in range(arr[i]+1,50):
                visited[j]=False

while True:
    lotto = list(map(int,input().split()))

    if lotto[0]==0:
        break
    else:
        visited = [False]*50
        comb = list()
        dfs(0,lotto[1:],comb)
        print()



