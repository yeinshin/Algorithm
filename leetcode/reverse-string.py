#https://leetcode.com/problems/reverse-string
#문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()