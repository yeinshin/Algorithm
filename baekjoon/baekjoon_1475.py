#https://www.acmicpc.net/problem/1475
#1475번-방 번호

from collections import Counter
from math import ceil
n=Counter(input().replace('9','6'))
n['6']/=2
print(ceil(max(n.values())))