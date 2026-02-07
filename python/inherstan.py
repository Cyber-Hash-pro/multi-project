class Factory:
    def __init__(self,cartype,typres,bodytype): 
        self.cartype = cartype 
        self.typres = typres 
        self.bodytype = bodytype 
        
    def show(self):
        print(f'This is a {self.cartype} car with {self.typres} type and {self.bodytype} body')
class Factory1:
    def __init__(self):
        print('hello')

class Honda(Factory):
    def __init__(self,cartype,typres,bodytype,model):
        super().__init__(cartype,typres,bodytype) # super() ka matlab hota hae parent class ko target karna and uske constructor ko call karna
        self.model = model
        
    def show(self):
        print(f'This is a {self.cartype} car with {self.typres} type and {self.bodytype} body and model is {self.model}')
        
Factory1 = Factory('suv',3,'sedan')
Factory1.show()
car1 = Honda('suv',3,'sedan','civic')
car1.show() # herer show method Honda ki run hogi 
# let suppose Honda apne ke liye ek Factory create karn thi but use pata nahi that ki Factory kiese banti hae to use ke Factory ko bola muje tume ler hae Factory ki proper
# to ye Factory ki propertly and age chaiye to extrach chije me khucd se create karnta hae 
# The multiple inheritance in python is a feature that allows a class to inherit from more than one parent class. This means that a child class can have multiple parent classes and can inherit attributes and methods from all of them. The syntax for multiple inheritance is as follows:

class Honda1(Factory,Factory1): # this multiple inheritance ka matlab hota hae ki Honda1 class Factory aur Factory1 dono se inherit kar rahi hai
    pass

# obj1 = Honda1() # here show  provide me cattype,typres,bodytype and hello method of Factory1 class
# but if show 
class Honda2(Factory1,Factory): # this multiple inheritance ka matlab hota hae ki Honda2 class Factory1 aur Factory dono se inherit kar rahi hai
    pass
obj2 = Honda2() # here show  provide me hello method of Factory1 class and cattype,typres,bodytype of Factory class