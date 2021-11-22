#https://www.acmicpc.net/problem/1897
#1897번-토달기
d,first = input().split()
first = list(first)
words = []
test = []
for _ in range(int(d)):
    w = list(input())
    test.append(w)
    words.append((len(w),w))
words.sort(key=lambda x:-x[0])

def dfs(t,origin,word):
    if len(origin)==len(word):
        if origin==word:
            print(''.join(word))
            exit()
        return
    for i in t:
        for j in range(len(origin)+1):
            if origin[0:j]+[i]+origin[j:] in test:
                dfs(t,origin[0:j]+[i]+origin[j:],word)
    
for l,word in words:
    t = []
    for w in word:
        if w not in first:
            t.append(w)
    dfs(t,first[:],word)