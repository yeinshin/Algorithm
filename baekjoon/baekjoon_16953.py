#16953번-A->B / 다시 풀어보기 

# a,b = map(int,input().split())
# count = 0

# def dfs(a,b,count):

#     if a>=b:
#         count = min(1e9,count)
#         return count
    
#     a*=2
#     dfs(a,b,count+1)
#     a=int(a/2)
#     count-=1

#     a=a*10+1
#     dfs(a,b,count+1)
#     a=int(a/10)-1
#     count-=1

# print(dfs(a,b,count))

from collections import deque

INF = int(1e9)

a, b = map(int, input().split())

ans = INF  # 정답
q = deque()
q.append((a, 0))  # 첫 위치 삽입

while q:
    dp, cnt = q.popleft()
    # dp가 b일 경우 정답 수정
    if dp == b:
        ans = min(ans, cnt)
        continue

    # dp가 b보다 작으면 2배와 1추가 과정후 삽입
    if dp < b:
        q.append((dp * 10 + 1, cnt + 1))
        q.append((dp * 2, cnt + 1))
    
    #if dp>b: 더이상 큐에 원소가 삽입x


# 도달 불가능
if ans == INF:
    print(-1)
# 도달 가능
else:
    print(ans + 1)