# Передаем строку ф-ии проверяем на уникальность символа 
# выводим индекс первого символа, если таких символов нет выводим -1
def first_unique_char(s):
    for i in s.lower():
        if s.count(i)==1:
            return s.index(i) 
    else:
        return(-1)   
a=input()
print(first_unique_char(a))
