#https://www.acmicpc.net/problem/1920
#1920번-수 찾기

n = int(input())
a = sorted(map(int,input().split()))
m = int(input())

def binary_search(start,end,target):
    while start<=end:
        mid = (start+end)//2
        if a[mid]==target or a[end]==target: return 1
        elif a[mid]>target: end = mid-1
        else: start = mid+1
    return 0

for t in list(map(int,input().split())):
    print(binary_search(0,n-1,t))