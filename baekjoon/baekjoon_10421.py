#https://www.acmicpc.net/problem/10421
#10421번-수식 완성하기

# 시간초과 코드 ㅜㅜ
# from itertools import product
# n = int(input())
# star = list(input().split())
# k = int(input())
# nums = list(input().split())
# result = set()
# for permu1 in product(nums,repeat = int(star[0])):
#     firstnum = int(''.join(permu1))
#     for permu2 in product(nums,repeat = int(star[1])):
#         secondnum=list(reversed(list(map(int,permu2)))) + [int(''.join(permu2))]
#         for i in range(len(secondnum)):
#             c = str(firstnum*secondnum[i])
#             check = False
#             if len(c)!=int(star[i+2]):
#                 break
#             for j in c:
#                 if j not in nums: 
#                     check = True
#                     break
#             if check: break
#         else: result.add((firstnum,int(''.join(permu2))))
# print(len(result))