def count_letters(a):
    N,K=0,0
    for i in a:
        N+=i.isupper()
        K+=i.islower()
    print(f'Количество заглавных символов: {N}\nКоличество строчных символов: {K}')
c=input()
count_letters(c)