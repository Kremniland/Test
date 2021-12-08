n=int(input())
a=[]
summa=0
for i in range(n):
    b=[]
    b=list(map(int,input().split()))
    a.append(b)
for i in range(n):
    for j in range(n):
        if i==j:
            summa+=a[i][j]
print(summa)