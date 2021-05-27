#https://www.acmicpc.net/problem/2661
#2661번-좋은수열/해설 참고함...다시 풀어보기

#sys.exit() vs exit()
# 둘은 비슷한 일을 하지만 쓰는 위치가 다릅니다.
# exit : interactive interpreter shell에서
# sys.exit : program에서
# Constants added by the site module에 적혀있길
# ... They are useful for the interactive interpreter shell and should not be used in programs.
# interactive interpreter shell에서 유용하게 쓰이고, 프로그램 안에서는 절대로 쓰면 안 됨

# 즉,파일에서
# #myfile.py - 파이썬 파일 안에서
# import sys
# exit()#안됨
# sys.exit() #됨

import sys

n = int(input())

def dfs(cnt,visited):

    if cnt == n:
        print(visited)
        sys.exit()

    for j in '123':
        if check(visited+j):
            dfs(cnt+1,visited+j)

def check(array):
    for i in range(1,(len(array)//2)+1):
        if array[-i:] == array[-2*i:-i]:
            return False
    return True

dfs(1,'1')
