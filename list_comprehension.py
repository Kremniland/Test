from string import ascii_uppercase
n=int(input())
#print(ascii_uppercase) # выведет строку ABCDEFGHIJKLMNOPQRSTUVWXYZ
#a=ascii_uppercase
b=[ascii_uppercase[i] for i in range(n)] #Заполнит список первыми  n буквами из ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(b)
