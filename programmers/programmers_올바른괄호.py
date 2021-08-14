#프로그래머스-올바른 괄호

def solution(s):
    test = list()
    
    for i in range(len(s)):
        if s[i] == '(':
            test.append('(')
        else:
            if len(test)!=0 and test[-1] == '(':
                test.pop()
            else: return False
            
    if len(test)!=0:
        return False
    return True