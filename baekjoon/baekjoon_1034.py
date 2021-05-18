#1034번-램프/ 다시 풀어보기
#1: 켜져있음
#0: 꺼져있음 
# import sys
# from itertools import combinations_with_replacement
# import copy

# input = sys.stdin.readline

# n,m = map(int,input().split())
# lamp = [[int(i) for i in input().rstrip()] for _ in range(n)]
# test = copy.deepcopy(lamp)
# k = int(input())
# comb = [i for i in range(m)]

# comb_list = list(combinations_with_replacement(comb,k))

# print(comb_list,end='\n\n')

# check = False
# result=0
# max_result = 0

# for j in comb_list:
#     for m in range(k):
#         for i in range(n):
#             if lamp[i][j[m]]==1:
#                 lamp[i][j[m]]=0
#             else:
#                 lamp[i][j[m]]=1

#     print(*lamp,sep='\n',end='\n\n')

#     # for x in range(n):
#     #     for y in range(m-1):
#     #         print('lamp[x][y]:',lamp[x][y],'and lamp[x][y+1]:',lamp[x][y+1],end='\n\n')
#     #         if lamp[x][y] == lamp[x][y+1] ==1:
#     #             check =True
#     #         else:
#     #             check=False

#     #     print(check,end='\n\n')
#     #     if check:
#     #         result+=1

#     # max_result= max(max_result,result)
#     # result = 0

# print(max_result)

# 입력받기
n, m = tuple(map(int, input().split()))
lst = []
for _ in range(n):
    lst.append(input())
    
k = int(input())

max_cnt = 0

# 모든 행에 대해 반복
for col in range(n):
    # 0의 개수 세기
    zero_count = 0
    for num in lst[col]:
        if num == '0':
            zero_count += 1
        
    # 이 행과 똑같은 값을 가진 행의 개수 세기
    col_light_cnt = 0
    if zero_count <= k and zero_count%2 == k%2:  # 이 행을 모두 킬 수 있다면
        for col2 in range(n):  # 다시한번 행을 반복하면서
            if lst[col] == lst[col2]:  # 두 개의 행이 같으면
                col_light_cnt += 1  # 1을 더해준다
                
    max_cnt = max(max_cnt, col_light_cnt)  # 최대값보다 크면 업데이트
    
print(max_cnt)