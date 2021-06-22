#https://www.acmicpc.net/problem/1912
#1912번-연속합/풀이 참고

n= int(input())
array = list(map(int,input().split()))
result = [array[0]]

for i in range(n-1):
    result.append(max(result[i]+array[i+1],array[i+1]))
print(max(result))    