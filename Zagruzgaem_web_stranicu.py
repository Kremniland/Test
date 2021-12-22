# загружает ВЕБ-страницу

from urllib.request import urlopen

# Адресс загружаемой ВЕБ-страницы:

html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')

# Переводим в STR:
s=str(html)
# Считаем сколько раз Python встретится на странице:
print(s.count('Python'))

#print(html)