#1759번-암호 만들기

from itertools import combinations 

#서로 다른 L개의 알파벳 소문자들로 구성
#문자의 종류는 C가지
l,c = map(int,input().split())
pwd = list(combinations(sorted(list(input().split())),l))

#암호를 저장할 리스트
pwd_result = list()

for p in pwd:
    cnt = 0
    check = False
    # 자음이 적어도 두개 이상있는지 check 해라
    for i in range(l):
        if p[i] not in ['i','a','e','o','u']:
            cnt +=1
        else:
            check = True
    # 모음이 있다는게 확인이 되면 리스트 삽입하고 for문 종료
    if 2<=cnt and check:
        pwd_result.append(''.join(p))

print(*pwd_result,sep='\n')