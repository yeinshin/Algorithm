#dfs로 만드는 순열

def permutations (selected,k):
    if k==N:
        print(' '.join(list(map(str,selected))))
    else:
        #1부터 N까지의 순열 생성
        for i in range(1,N+1):
            print('if문 전: i=',i,'k:',k)
            print('if문 전: selected=',selected)
            if i not in selected:
                # ex) selected = [1], [i] = [2] -> [1]+[2]=[1,2] => selected.append(i)와 같다.
                print('if문 후: i=',i,'k:',k)
                permutations(selected+[i],k+1)
                print('if문 전: selected=',selected)

N=int(input())
permutations([],0)