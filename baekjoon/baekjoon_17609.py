#https://www.acmicpc.net/problem/17609
#17609번-회문/시간초과나서 풀이 참고
import sys

input = sys.stdin.readline

def first_check(s,left,right):
    while left < right:
        if s[left] == s[right]:
            left +=1
            right -=1
        else:
            check1 = second_check(s,left+1,right)
            check2 = second_check(s,left,right-1)

            if check1 or check2: return 1
            else: return 2
    return 0

def second_check(s,left,right):
    while left < right:
        if s[left]==s[right]:
            left+=1
            right-=1
        else: return False
    
    return True

for _ in range(int(input())):
    s = input().rstrip()
    print(first_check(s,0,len(s)-1))

















#---------------------------------------------------------------------------------
#시간초과 코드

# import sys
# input = sys.stdin.readline
# for _ in range(int(input())):
#     array = input().rstrip()
#     check = False

#     if array == array[::-1]:
#         print(0)
#     else:
#         for i in range(len(array)):
#             new_array = array[:i]+array[i+1:]
#             if new_array[::-1] == new_array:
#                 check = True
#                 break
#         if not check :
#             print(2) 

