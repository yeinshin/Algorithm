#https://www.acmicpc.net/problem/5052
#5052번-전화번호 목록

for _ in range(int(input())):
    n = int(input())
    num = sorted([input() for _ in range(n)])
    check = False
    for i in range(n-1):
        if num[i]==num[i+1][:len(num[i])]: check = True #상대문자열길이만큼 앞부분이 같지 않으면 pass
    print('NO' if check else 'YES')