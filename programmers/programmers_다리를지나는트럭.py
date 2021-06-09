#https://programmers.co.kr/learn/courses/30/lessons/42583
#프로그래머스-다리를 지나는 트럭/풀이 참고함 ㅜ 

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)

    while bridge:
        bridge.popleft()
        answer+=1

        if truck_weights:
            if sum(bridge)+truck_weights[0]<=weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return answer