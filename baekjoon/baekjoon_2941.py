#https://www.acmicpc.net/problem/2941
#2941번-크로아티아 알파벳
print(len(input().replace('c=','0').replace('c-','0').replace('dz=','0').replace('d-','0').replace('lj','0').replace('nj','0').replace('s=','0').replace('z=','0')))
# test = ['c=','c-','dz=','d-','lj','nj','s=','z=']
# s = input()
# result = 0
# check = 0
# start = 0
# end = 2
# while 1:
#     if end>len(s): break
#     if s[start:end] in test:
#         check+=len(s[start:end])
#         start=end
#         result+=1
#     elif s[start:end]!='dz' and end-start==2: start+=1
#     end+=1
# print(result+len(s)-check)