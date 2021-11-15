#https://www.acmicpc.net/problem/4659
#4659번-비밀번호 발음하기

while 1:
    pw=input()
    if pw=='end':break
    check = False
    for i in range(len(pw)):
        if pw[i] in ('a','e','i','o','u'): check = True
    if check:
        for i in range(len(pw)-2):
            if (pw[i] in ('a','e','i','o','u') and pw[i+1] in ('a','e','i','o','u') and pw[i+2] in ('a','e','i','o','u')) or (pw[i] not in ('a','e','i','o','u') and pw[i+1] not in ('a','e','i','o','u') and pw[i+2] not in ('a','e','i','o','u')):
                print('<%s> is not acceptable.'%pw)
                break
        else:
            for i in range(len(pw)-1):
                if pw[i]==pw[i+1] and pw[i] not in ('e','o'):
                    print('<%s> is not acceptable.'%pw)
                    break
            else: print('<%s> is acceptable.'%pw)
    else:print('<%s> is not acceptable.'%pw)