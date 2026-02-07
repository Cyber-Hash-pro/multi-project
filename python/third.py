#----------------------------------------------------------
# funcation in python
# print aslo is a funcation in python
# (# syntax of funcation) ()-> this is used to call the funcation
# USER DEFINED FUNCATION
# def define a funcation
# syntax : -> def funcation_name(parameters):
def hello():
    print('hello world')
# hello()  # call the funcation output will be hello world
hello()
# ----------------------------------------------------------
# funcation hamesh 2 chije hote hae ek hae parameters aur dusra hota hae aggrument
# parameters -> ye funcation ke andar hota hae jab hum funcation ko define karte hae
# aggrument -> ye funcation ko call karte waqt use hota hae
def greet(name):  # name is parameter
    print('hello ' + name)
greet('nilesh')  # 'nilesh' is aggrument
greet('test')
# default parameter in funcation here c=1 is default parameter
def numb(a,b,c=1):
    print('a:',a)
    print('b:',b)
    print('c:',c)
numb(5,6)  # here c will take default value 1
numb(7,8,9)  # here c will take value 9
# default  agrument vs keyword agrument
def hello1(a,b,c):
    print(f'a:{a}, b:{b}, c:{c}')
hello1(1,2,3)  # here default  agrument 
hello1(c=3,b=2,a=1)  # here we use keyword agrument apne apne  position  chale jayega

# ----------------------------------------------------------
# return statement in funcation
# print vs return
def add(a,b):
    return a+b  # return statement return karne use call karte waqt ek variable me store kar sakte hae and use answer nikal sakte 
result = add(5,7)
print('result:',result) 
def sub(a,b):
    print(a-b)  # print statement
result1 = sub(10,4)
print('result1:',result1)  # here result1 will be None because sub funcation me return nhi hae
# ----------------------------------------------------------
# Strings in python
v ='helloworld'
 # first talk on string indexing
# indexing start from 0 in python   indexing meeans index
print(v[0])  # h
print(v[4])  # o
print(v[-1]) # d
print(v[8])  # r
# string Slicing
Slicing= 'helloworld'
print(Slicing[0:5])  # hello  (start index se leke end index-1 tak) 
print(Slicing[5:10]) # world
print(Slicing[:5])   # hello (agar start index nhi diya to by default 0 se start hoga)
print(Slicing[0:7:2]) # hlo ol (step value 2) like range function
# len() function in string
lenth='nilesh'
lenths='nilesh patil'
print(len(lenth))  # 6
print(len(lenths)) # 12 (space bhi count hota hae)
# ----------------------------------------------------------
# 2 way of iterating string over string
string_iterate = 'nilesh'
# 1st way using for loop
# for char in string_iterate:
#     print(char)
# 2nd way using while loop
for i in string_iterate:
    print(i)
for i in range(len(string_iterate)):
    print(string_iterate[i])        
# i=0
# while i < len(string_iterate):
#     print(string_iterate[i])
#     i += 1
# ----------------------------------------------------------
# cheak Sting
check_string = 'hello world'
# check if 'hello' is present in check_string
if 'hello' in check_string: # hello is present in check_string is true  but 'hello  ' 2 space is not present false
    print('yes hello is present')
#----------------------------------------------------------
# string method in python
string_methods = '  hello world  '
print(string_methods.upper())  # HELLO WORLD
print(string_methods.lower())  # hello world
print(string_methods.strip())  # hello world (remove space from start and end)
print(string_methods.replace('world','there'))  # hello there
print(string_methods.split())  # ['hello', 'world'] (split by space)
# ----------------------------------------------------------
