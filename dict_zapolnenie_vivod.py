from string import ascii_lowercase
alphabet={}

for i in range(len(ascii_lowercase)):
    alphabet.setdefault(i+1, ascii_lowercase[i])


for i in alphabet.items():
    print(*i)
