n,m=map(int,input().split())
a=[]
s=0

# Ввод списка с клавиатуры:
for i in range(n):
    a.append(list(map(int,input().split())))

# Вывод матрицы с подсчетом суммы в строках и в столбцах:
for i in range(n):
    for j in range(m):
        s+= A[i][j]
    print(s, end=" ")
    s = 0
print()
for j in range(m):
    for i in range(n):
        s+= A[i][j]
    print(s, end= " ")
    s = 0
