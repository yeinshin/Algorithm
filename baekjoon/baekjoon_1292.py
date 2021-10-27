#https://www.acmicpc.net/problem/1292
#1292번-쉽게 푸는 문제
a,b = map(int,input().split())
nums = []
start = 1
while 1:
    nums.extend([start]*start)
    if len(nums)>=b:
        print(sum(nums[a-1:b]))
        break
    start+=1
