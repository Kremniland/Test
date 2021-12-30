class Laptop:
    def __init__(self, brand='', model='', price=0):
        self.brannd=brand
        self.laptop_name=model
        self.price=price


hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price)  # выводит 57000
print(hp.laptop_name)  # выводит "hp 15-bw0xx"
laptop1 = Laptop()
laptop2 = Laptop()
