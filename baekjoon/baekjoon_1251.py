#https://www.acmicpc.net/problem/1251
#1251번-단어 나누기
from itertools import combinations
word = list(input())
result=[]
for start,mid in combinations(range(1,len(word)),2):
    a=word[:start]
    b=word[start:mid]
    c=word[mid:]
    result.append(''.join(a[::-1]+b[::-1]+c[::-1]))
print(sorted(result)[0])
    