#https://programmers.co.kr/learn/courses/30/lessons/42586
#프로그래머스-기능개발
import math
def solution(progresses, speeds):
    answer = []
    stack = list()
    for i in range(len(progresses)):
        if not stack:
            stack.append(math.ceil((100-progresses[i])/speeds[i]))
            answer.append(1)
        else:
            if stack[-1] >= math.ceil((100-progresses[i])/speeds[i]):
                answer[-1]+=1
            else:
                stack.append(math.ceil((100-progresses[i])/speeds[i]))
                answer.append(1)
    return answer
