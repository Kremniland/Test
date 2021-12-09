a,b=map(int,input().split())

if a<=b:        
    l=[i**2 for i in range(a,b)]        #Если а<=b заполняем квадратами чисел от а до б
else:
    l=[i**3 for i in range(a,b,-1)]     #Если а<b заполняем кубами от а до б шагом -1
    
print(l)
