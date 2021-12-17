#https://www.acmicpc.net/problem/1107
#1107번-리모컨/다시 풀어보기
#수빈이가 지금 보고 있는 채널은 100번이다.

#채널 번호
N = int(input())
#고장난 버튼의 수
M = int(input())

#고장난 버튼이 존재하는 경우
if M != 0:
    B = list(input().split())
#고장난 버튼이 없는 경우 빈 리스트로 선언
else:           
    B = []

#고장난 버튼을 제외한 버튼 리스트 생성
R = [str(i) for i in range(10) if str(i) not in B]

result = abs(N - 100)
for i in range(1000000):
    tf = True
    for s in str(i):
        if s not in R:
            tf = False
            break
    if tf:
        #여기서 abs(N-i)를 해주는 이유는 + 버튼이나 - 버튼을 눌렀을때의 횟수
        #len(str(i))는 숫자 버튼 누른 횟수
        result = min(result, abs(N - i)+len(str(i)))
print(result)


