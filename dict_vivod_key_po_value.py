# Найти какой стране принадлежит введенный город:

countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()

for k, v in countries.items():
    if city in v:
        print(f'INFO: {city} is a city in {k}') # Если принадлежит
        break
    
else:
    print(f'ERROR: Country for {city} not found') #  Если не принадлежит
    
        
        