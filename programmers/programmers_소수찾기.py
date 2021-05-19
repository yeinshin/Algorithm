#프로그래머스-소수 찾기

from itertools import permutations

def solution(numbers):
    answer = 0
    
    number = list(numbers)
    
    num_list = list()
    
    # print('len(number):',len(number))
    for i in range(1,len(number)+1):
        # print('i:',i)
        
        number_permu = list(set(permutations(number,i)))
        
        for num in number_permu:
            n = int(''.join(list(map(str,num))))
            # print(n,end='\n\n')
            
            if n >= 2:
                check = False
                for j in range(2,n):
                    if n%j==0:
                        check = True
                        if check:
                            break

                if not check and n not in num_list:
                    num_list.append(n)
    
    print(num_list,end='\n\n')
    print(len(num_list))
    return len(num_list)


solution('123123')