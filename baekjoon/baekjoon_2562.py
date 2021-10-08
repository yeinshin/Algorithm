#https://www.acmicpc.net/problem/2562
#2562번-최댓값

num = [int(input()) for _ in range(9)]
print(max(num),num.index(max(num))+1,sep='\n')