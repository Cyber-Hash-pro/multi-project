class Factory:
    a = 12
    b = 23

object1 = Factory() # object1 ek object and and object kya power hae jo bhi class ke pass power hota hae wo object ke pass hota hae 
print(object1.a)  # 12
print(object1.b)  # 23  
# in python contructor jise kuch nahi hota use me ham bolte hae intionalization 
def fucnFactory(cartype,typres,bodytype):
    print(f'This is a function factory',cartype,typres,bodytype)
fucnFactory('suv','petrol','sedan')


class Factory1:
    def __init__(self): # ese kya hova ab hae ban kucha hae contrucator funcation  and jise aap Factory1() call karoge to ye __init__ function automatically call hoga  and __init__ function ke andar jo bhi code hoga wo run hoga
     print("This is constructor of Factory1 class") # contrucaton mean automatically call hone wala ahe jab class chale
    
object2 = Factory1() # jab bhi aap Factory1() call karoge to ye __init__ function automatically call hoga  and __init__ function ke andar jo bhi code hoga wo run hoga     

class Factory2:
    def __init__(self,cartype,typres,bodytype): # in here self apne object ko target karnata hae 
        self.cartype = cartype # hame pata ki self ka mtlab ek memory ke address data hold karna hae hamne ap self. karke udar use bola ki ek chij tere pass store karna hae  memory me
        self.typres = typres # self.typres ka matlab hota hae apne object ke typres attribute ko target karna and typres is parameter of constructor function
        self.bodytype = bodytype # java per self diya to wo hota hae ek object and hame use bolte he object artribute  slef ==object
        
        
        
        print(f'This self is show memory address of object',self) # self ka matlab hota hae apne object ko target karna
        print(f'This is a constructor of Factory2 class',cartype,typres,bodytype)  
object3 = Factory2('suv',3,'sedan') # maltab jo tum class kko class karge tab udar wo parameter ke class value mnage gya object 3 is obj
# what is self in python
print(object3) # object3 ka memory address show karega jo self and object3 same memory address show karega
print(object3.typres) 