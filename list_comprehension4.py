phrase = 'Take only the words that start with t in this sentence'.split()
a=[i for i in phrase if i[0].upper()=='T'] #Выбирает из фразы слова на Т или т
print(a)