a=input()
c='0123456789'
b=len(a)
sum=0
k=0
for i in range(b):
    if a[i] in c:
        sum+=1
        k+=int(a[i])

print(sum, k)