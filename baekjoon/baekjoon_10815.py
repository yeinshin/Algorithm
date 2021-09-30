#https://www.acmicpc.net/problem/10815
#10815번-숫자 카드
n = int(input())
card = sorted(map(int,input().split()))
m = int(input())

def binary_search(start,end,target):
    while start<=end:
        mid = (start+end)//2
        if card[mid]==target: return 1
        elif card[mid]<target:start = mid +1
        else: end = mid -1
    return 0

for t in list(map(int,input().split())):
    print(binary_search(0,n-1,t))