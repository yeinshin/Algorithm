#https://www.acmicpc.net/problem/1244
#1244번-스위치 켜고 끄기

switch = int(input())
state = list(map(int,input().split()))
student = int(input())
students = [list(map(int,input().split())) for _ in range(student)]

for s in students:
    if s[0]==1: #남학생일때
        for i in range(1,switch+1):
            if i%s[1]==0:
                if state[i-1]==1:
                    state[i-1]=0
                else:
                    state[i-1]=1
    
    elif s[0]==2: #여학생일때
        for i in range(s[1],switch):
            if state[i]==state[((s[1]-1)-(i-(s[1]-1)))]and 0<=((s[1]-1)-(i-(s[1]-1))):
                if state[i]==1:
                    state[i]=0
                    state[((s[1]-1)-(i-(s[1]-1)))]=0
                else:
                    state[i]=1
                    state[((s[1]-1)-(i-(s[1]-1)))]=1
            else:
                break
        
        if state[s[1]-1]==1:
            state[s[1]-1]=0
        else:
            state[s[1]-1]=1


for i in range(switch):
    if i!=0 and i%20==0:
        print()
    print(state[i],end=' ')



