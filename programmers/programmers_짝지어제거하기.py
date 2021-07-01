#https://programmers.co.kr/learn/courses/30/lessons/12973
#프로그래머스-짝지어 제거하기/풀이 방법 참고함

def solution(s):
    stack = []
    
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if stack [-1]!=s[i]:
                stack.append(s[i])
            elif stack[-1]==s[i]:
                stack.pop()
        
    if len(stack)>0: return 0
    else: return 1