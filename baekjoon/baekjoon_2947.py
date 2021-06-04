#https://www.acmicpc.net/problem/2947
#2947번-나무 조각

tree = list(map(int,input().split()))

while tree!=[1,2,3,4,5]:
    for i in range(len(tree)-1):
        if tree[i]>tree[i+1]:
            tree[i],tree[i+1]=tree[i+1],tree[i]
            print(*tree,sep=' ')
    