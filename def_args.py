def print_goods(*args):
   cout=0
   for i in args:
       if type(i)==str and len(i) != 0:
           cout+=1
           print(f'{cout}. {i}')
   if cout==0:
       print('Нет товаров')
    
print_goods(1, True, 'Грушечка', '', 'Pineapple')
