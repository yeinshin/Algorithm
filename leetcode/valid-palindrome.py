#https://leetcode.com/problems/valid-palindrome/submissions/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        test = list()
        for c in s:
            if c.isalnum():
                test.append(c.lower())
        return test == test[::-1]