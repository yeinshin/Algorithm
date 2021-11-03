#https://www.acmicpc.net/problem/7490
#7490번-0 만들기
import re
t = int(input())
for i in range(t):
    n = int(input())
    result = []
    def calc(s):
        if ' ' in s: s = s.replace(' ','')
        notnum = re.findall('[+-]',s)
        nums = list(map(int,re.findall('[0-9]+',s)))
        cnt = nums[0]
        for c in range(len(notnum)):
            if notnum[c]=='+': cnt+=nums[c+1]
            else:cnt-=nums[c+1]
        return True if cnt==0 else False

    def dfs(cnt,s):
        if cnt==n:
            if calc(s) : 
                result.append(s)
            return
        for j in ('+','-',' '):
            dfs(cnt+1,s+j+str(cnt+1))
    dfs(1,'1')
    if i!=t-1:
        print(*sorted(result),sep='\n',end='\n\n')
    else: print(*sorted(result),sep='\n')
