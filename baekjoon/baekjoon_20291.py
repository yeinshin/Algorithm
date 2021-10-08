#https://www.acmicpc.net/problem/20291
#20291번-파일 정리
from collections import Counter
n = int(input())
files = sorted(Counter([input().split('.')[1] for _ in range(n)]).items())
for a,b in files:print(a,b)
    

