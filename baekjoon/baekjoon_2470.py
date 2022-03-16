# https://www.acmicpc.net/problem/2470
# 2470번-두 용액

import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(map(int, input().split()))

ans = []
check = sys.maxsize
start, end = 0, n-1
while start < end:
    mix = abs(arr[start]+arr[end])
    if mix == 0:
        print(arr[start], arr[end])
        break
    ans.append((mix, arr[start], arr[end]))
    if mix > check:
        start += 1
    else:
        end -= 1
    check = min(check, mix)


else:
    ans.sort()
    print(ans[0][1], ans[0][2])
