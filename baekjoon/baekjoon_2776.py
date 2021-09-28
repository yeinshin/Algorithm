#https://www.acmicpc.net/problem/2776
#2776번-암기왕
for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int,input().split()))
    m = int(input())
    target = list(map(int,input().split()))

    def binary_search(start,end,t):
        while start<=end:
            mid = (start+end)//2
            if a[mid]==t:return 1
            elif a[mid]<t:start=mid+1
            else:end=mid-1
        return 0
    for t in target: 
        print(binary_search(0,n-1,t))
        