#https://www.acmicpc.net/problem/13335
#13335번-트럭/풀이 참고함 ㅜ
#n은 다리를 건너는 트럭의 수, w는 다리의 길이, 그리고 L은 다리의 최대하중을 나타낸다.
from collections import deque

n,w,L = map(int,input().split())
truck = list(map(int,input().split()))
bridge = deque([0]*w)
cnt=0

while bridge:
    bridge.popleft()
    cnt+=1

    if truck:
        if sum(bridge)+truck[0]<=L:
            bridge.append(truck.pop(0))
        else:
            bridge.append(0)

print(cnt)