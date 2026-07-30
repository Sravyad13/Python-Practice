class Car:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def apply_discount(self,discount_percentage):
        self.price=self.price-(self.price*discount_percentage/100)

tesla=Car("ModelY",25000)        
print(tesla.name)
tesla.apply_discount(10)
print(tesla.price)