#https://www.acmicpc.net/problem/1342
#1342번-행운의 문자열
from collections import Counter
s = input()
cnt_s = Counter(s)
result = 0
def back(cnt,lucky):
    global result
    if cnt == len(s):
        result+=1
        return
    for i in cnt_s.keys():
        if lucky==i or cnt_s[i]==0:continue
        cnt_s[i]-=1
        back(cnt+1,i)
        cnt_s[i]+=1
back(0,'')
print(result)