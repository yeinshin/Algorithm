#https://www.acmicpc.net/problem/16198
#16198번-에너지 모으기

n=int(input())
balls=list(map(int,input().split()))
max_energy = 0

def dfs(energy):
    global max_energy

    if len(balls)==2:
        max_energy = max(max_energy,energy)
        return 

    for i in range(1,len(balls)-1):
        now=balls[i]
        energy+=balls[i-1]*balls[i+1]
        balls.pop(i)
        dfs(energy)
        balls.insert(i,now)
        energy-=balls[i-1]*balls[i+1]
            
dfs(0)
print(max_energy)
