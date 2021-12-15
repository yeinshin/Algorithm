#https://www.acmicpc.net/problem/5568
#5568번-카드 놓기
from itertools import permutations
n = int(input())
k = int(input())
card = []
for _ in range(n):
    a = input()
    card.append(a)
result = set()
for permu in permutations(card,k):
    result.add(''.join(permu))
print(len(result))
