#https://www.acmicpc.net/problem/16637
#16637번-괄호 추가하기
from itertools import combinations
import math
n = int(input())
s = input()
calc,nums = [],[]
result = -2**31
if n==1: print(s)
else:
    for i in range(len(s)):
        if not s[i].isdigit():calc.append(s[i])
        else: nums.append(int(s[i]))

    for i in range(1,math.ceil(len(calc)/2)+1):
        for comb in combinations(range(len(calc)),i):
            copy_nums = nums[:]
            copy_calc = calc[:]
            check = True
            for j in range(len(comb)-1):
                if abs(comb[j]-comb[j+1])==1:
                    check=False
                    break
            if check:
                for j in range(len(comb)):
                    if calc[comb[j]]=='+':
                        copy_nums[comb[j]+1]=nums[comb[j]]+nums[comb[j]+1]
                        copy_nums[comb[j]]='x'
                        copy_calc[comb[j]]='x'
                    elif calc[comb[j]]=='-':
                        copy_nums[comb[j]+1]=nums[comb[j]]-nums[comb[j]+1]
                        copy_nums[comb[j]]='x'
                        copy_calc[comb[j]]='x'
                    else: #'*'
                        copy_nums[comb[j]+1]=nums[comb[j]]*nums[comb[j]+1]
                        copy_nums[comb[j]]='x'
                        copy_calc[comb[j]]='x'
                final_calc=[]
                final_nums=[]
                for j in range(len(copy_calc)):
                    if copy_calc[j]!='x':
                        final_calc.append(copy_calc[j])
                        final_nums.append(copy_nums[j])
                final_nums.append(copy_nums[-1])
                cnt = final_nums[0]
                for j in range(len(final_calc)):
                    if final_calc[j]=='+':
                        cnt+=final_nums[j+1]
                    elif final_calc[j]=='-':
                        cnt-=final_nums[j+1]
                    else: cnt*=final_nums[j+1]
                result = max(result,cnt)
    print(result)