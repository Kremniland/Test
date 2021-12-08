n=int(input())
a=[]
for i in range(n):
    b=[]
    b=list(map(int,input().split()))
    a.append(b)
for i in range(n):
    for j in range(n):
        print(a[j][i],end=' ')
    print()
