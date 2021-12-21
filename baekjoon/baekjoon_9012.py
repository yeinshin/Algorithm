#https://www.acmicpc.net/problem/9012
#9012번-괄호
for _ in range(int(input())):
    s = input()
    stack = []
    check = False
    for i in s:
        if i==')':
            if stack and stack[-1]=='(': stack.pop()
            else:
                check = True
                break
        else:stack.append('(')
    print('NO' if check or stack else 'YES')