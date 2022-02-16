#https://www.acmicpc.net/problem/1477
#1477번-휴게소 세우기
import heapq
from statistics import harmonic_mean
n,m,l = map(int,input().split())
arr = [0]+sorted(map(int,input().split()))+[l]
d = []
for i in range(n+1):
    a = arr[i+1]-arr[i]
    heapq.heappush(d,(-a,1))
while m>0:
    a,div = heapq.heappop(d)
    og = abs(a*div)
    half =og/(div+1)
    if og%(div+1)!=0: heapq.heappush(d,(-(int(half)+1),div+1))
    else: heapq.heappush(d,(-int(half),div+1))
    m-=1

print(abs(heapq.heappop(d)[0]))