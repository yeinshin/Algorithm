#https://www.acmicpc.net/problem/16922
#16922번-로마 숫자 만들기
from itertools import combinations_with_replacement
print(len(set(map(sum,list(combinations_with_replacement([1,5,10,50],int(input())))))))