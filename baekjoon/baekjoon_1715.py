#https://www.acmicpc.net/problem/1715
#1715번-카드 정렬하기

import heapq
n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)
if len(cards)==1: print(0)
else:
    ans = 0
    while len(cards)>1:
        v1=heapq.heappop(cards)
        v2=heapq.heappop(cards)
        ans+=v1+v2
        heapq.heappush(cards,v1+v2)
    print(ans)