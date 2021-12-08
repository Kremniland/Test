a=int(input())
l=list(map(int,input().split()))
count=0
count1=1
while count1>0:
    count1=0
    for i in range(a-1):
        if l[i]<l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
            count+=1
            count1+=1
for i in range(a):
    print(l[i])
print(count)

