# https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        
        stck = list()
        test = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        
        for i in s:
            if i not in test.keys():
                stck.append(i)
            elif stck and stck[-1]==test[i]:
                stck.pop()
            else: return False
            
        
        if len(stck)==0:
            return True
        else: return False