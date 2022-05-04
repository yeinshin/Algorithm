#https://www.acmicpc.net/problem/2922
#2922번-즐거운 단어

# w = input()
# n = len(w)
# ans = 0
# words = ['']*n
# check = False

# for i in range(n):
#     if w[i]!='_': words[i] = w[i]
#     if w[i]=='L': check = True

# def backtracking(idx,j,m,cnt,check):
#     global ans,n
#     if j>=3 or m>=3: return
#     if idx==n:
#         if check:
#             ans+=cnt
#         return

#     if words[idx]!='':
#         if words[idx] in ['A','E','I','O','U']: backtracking(idx+1,0,m+1,cnt,check)
#         else: 
#             backtracking(idx+1,j+1,0,cnt,check)
#     else:
#         backtracking(idx+1,0,m+1,cnt*5,check)
#         if not check:
#             backtracking(idx+1,j+1,0,cnt*20,check)
#             backtracking(idx+1,j+1,0,cnt,True)
#         else: backtracking(idx+1,j+1,0,cnt*21,check)
        
# backtracking(0,0,0,1,check)
# print(ans)

w = input()
n = len(w)
ans = 0
check = True if 'L' in w else False

def backtracking(idx,j,m,cnt,check):
    global ans,n
    if j>=3 or m>=3: return
    if idx==n:
        if check:
            ans+=cnt
        return

    if w[idx]!='_':
        if w[idx] in ['A','E','I','O','U']: backtracking(idx+1,0,m+1,cnt,check)
        else: 
            backtracking(idx+1,j+1,0,cnt,check)
    else:
        backtracking(idx+1,0,m+1,cnt*5,check)
        if not check:
            backtracking(idx+1,j+1,0,cnt*20,check)
            backtracking(idx+1,j+1,0,cnt,True)
        else: backtracking(idx+1,j+1,0,cnt*21,check)
        
backtracking(0,0,0,1,check)
print(ans)