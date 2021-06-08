#https://www.acmicpc.net/problem/1713
#1713번-후보 추천하기

n= int(input())
r = int(input())
students = list(map(int,input().split()))
photo = list()
recommend = [0] * 101

for s in students:
    recommend[s]+=1 #추천을 받으면 무조건 추천수가 1씩 증가
    if s in photo:
        continue
    else:
        if len(photo)==n and s not in photo:
            min_student=100
            for i in range(n):
                min_student=min(min_student,recommend[photo[i]])
            for i in range(n):
                if recommend[photo[i]]==min_student:
                    recommend[photo[i]]=0
                    del photo[i]
                    break 
        photo.append(s)

print(*sorted(photo),sep=' ')