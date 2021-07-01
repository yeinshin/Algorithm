#https://leetcode.com/problems/longest-palindromic-substring/

def longestPalindrome(self,s:str) -> str:

    #팰린드롬 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right +=1 
        
        return s[left+1:right]
    

    if len(s)<2 or s==s[::-1]:
        return s
    
    result = ''

    for i in range(len(s)-1):
        # key = len의 의미: 가장 긴 것을 골라라
        result = max(result,expand(i,i+1),expand(i,i+2),key=len)