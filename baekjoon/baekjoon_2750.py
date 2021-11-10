#https://www.acmicpc.net/problem/2750
#2750번-그대로 출력하기
n = int(input())
num = [int(input()) for _ in range(n)]
print(*sorted(num),sep='\n')