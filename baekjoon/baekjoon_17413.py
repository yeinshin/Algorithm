#https://www.acmicpc.net/problem/17413
#17413번-단어 뒤집기2
import sys
input = sys.stdin.readline
s = input().rstrip()
result = list()
i = 0

def re (array):
    array = array.split()
    for i in range(len(array)):
        array[i]=array[i][::-1]
    result.append(' '.join(array))

if '<' not in s:
    re(s)
else:
    while i < len(s):
        if s[i]=='<':
            for j in range(i,len(s)):
                if s[j]=='>':
                    result.append(s[i:j+1])
                    i=j+1
                    break
        else:
            change = []
            for a in range(i,len(s)):
                if s[a]=='<':
                    i = a
                    break
                change.append(s[a])
                if a==len(s)-1:
                    i = len(s)
                    break
            re(''.join(change))

print(''.join(result))