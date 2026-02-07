class Factory1:
    
    def hello():
        print("hello world from Factory1 class")

car1=Factory1.hello()

class Factory2:
    def __init__(self,cartype,typres,bodytype):
        self.cartype=cartype
        self.typres=typres
        self.bodytype=bodytype
        print(f'This is a constructor of Factory2 class',cartype,typres,bodytype)
    
    def hello():
        print("hello world every car")
    def hello2(self):
        print(f'hello world from car type {self.cartype} {self}')
        
        
car2=Factory2('suv',3,'sedan')
# but agar mene car3.hello() call kiya to ek error aayega
# error is TypeError: hello() takes 0 positional arguments but 1 was given 
# first eska matlab kya hota hae mean car3.hello() jab esa karto hae to car3 ek object hota hae and wo apne aap ko as a first argument hello method ko pass kar deta hae

# car2.hello1() error aayega TypeError: hello1() takes 0 positional arguments but 1 was given
car2.hello2()  # object 2 ek argument ke sath hello2 chalta jtateand agar apne self nahi likha to wo error deta hai hello2() takes 0 positional arguments but 1 was given