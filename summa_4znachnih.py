a=list(map(int,input().split()))
for i in range(len(a)):
    for j in range(a[i]):
        print('*',end='')
    print()