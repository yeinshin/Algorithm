#https://www.acmicpc.net/problem/10816
#10816번-숫자 카드 2
from collections import defaultdict
n = int(input())
card = sorted(map(int,input().split()))
card_dict = defaultdict(int)
for c in card:
    card_dict[c]+=1
m = int(input())
for t in list(map(int,input().split())):
    result = 0
    start,end = 0,n-1
    while start<=end:
        mid = (start+end)//2
        if card[mid]==t: break
        elif card[mid]<t:start = mid +1
        else: end = mid -1
    print(card_dict[t] if card[mid]==t else 0,end=' ')