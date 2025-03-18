class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,order2):
        return self.price > order2.price
    
    def __lt__(self,order2):
        return self.price < order2.price
    

order1 = Order('lays',20)
order2 = Order('tea',10)

print(order1 > order2)
print(order1 < order2)