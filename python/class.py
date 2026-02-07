# create the class
class Factory:
    a=12 # a is not variable it is class attribute jab bhi ap class ke andar variable banate hae to wo class attribute ban jata hae
    b=23
    print("This is Factory class",a,b) # ye line
    def hello(): # this is method of class  like ek class ke andar function hota hae to wo method hota hae
        print("hello world")
    # next part is public and private
    c=12 # c is public attribute of class Factory matlab c ko hum class ke bahar se bhi access kar sakte hae
    # to create private use encapsulation
    __d=23 # d is private attribute of class Factory matlab d ko hum class ke bahar se access nahi kar sakte hae 
    def __helloprivate(): # this is private method of class Factory matlab __hello ko hum class ke bahar se access nahi kar sakte hae 
        print("This is private method")
    __helloprivate() # ye class ke andar andar and private hae to work hoga private sirf class me hi accessable hot ahae
    

print(type(Factory()))  # <class '__main__.Factory'>

Factory() #
print(Factory.c) # here c is public attribute of class Factory so we can access it using class name and dot operator
print(Factory.hello()) # here hello is method of class Factory so we can access it using class name and dot operator hello is public method of class Factory so we can access it using class name and dot operator
# print(Factory.__d) # here __d is private attribute of class Factory so we cannot access it using class name and dot operator it will give error
# print(Factory.__helloprivate()) # here __helloprivate is private method of class Factory so we cannot access it using class name and dot operator it will give error