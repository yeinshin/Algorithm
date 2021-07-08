#https://programmers.co.kr/learn/courses/30/lessons/76502
#프로그래머스-괄호 회전하기/풀이 참고함

def solution(s):
    answer = -1
    
    def check(s):
        stack = []
        for a in s:
            if a in ('(','[','{'):
                stack.append(a)
            else:
                if not stack:
                    return 0

                before = stack.pop()
                if a==')' and before!='(':
                    return 0
                if a==']' and before!='[':
                    return 0
                if a=='}' and before!='{':
                    return 0
        if not len(stack):
            return 1
        else: return 0
            
    for i in range(len(s)):
        if i==0:
            answer=check(s)
        else:
            s = s[1:]+s[0:1]
            answer+=check(s)
             
    return answer