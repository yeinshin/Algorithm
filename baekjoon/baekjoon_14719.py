# https://www.acmicpc.net/problem/14719
#14719번-빗물

#2차원 세계의 세로 길이 H과 2차원 세계의 가로 길이 W (blocks 리스트 길이와 같음)
h,w = map(int,input().split())
blocks = list(map(int,input().split()))
result = 0
for i in range(1,w-1):
    minb=min(max(blocks[:i]),max(blocks[i+1:]))
    if blocks[i]<minb:
        result+= minb - blocks[i]
print(result)