#Выводит первые список из первых букв данной строки

st = 'Create a list of the first letters of every word in this string'
a=[]
a=st.split()  #Заполняем список словами, разбивая строку по пробелам
b=[]
b=[a[i][0] for i in range(len(a))] #Заполняем список первыми буквами слов
print(b)