# List 
# A list is a versatile data structure in Python that can hold an ordered collection of items.
# Lists are mutable, meaning you can change their content without changing their identity.
# You can create a list using square brackets [] and separate items with commas.
# my_list = [10, 20, 30, 40, 50]
# print('Original List:', my_list)
# why list is versatile?
# because it can hold different data types together like integer, string, float, function ,boolean, and even other lists.
# my_list2 = [1, 'hello', 3.14, True, [5, 6, 7]]
# print('Versatile List:', my_list2)
# what is mutable? and list is mutable
# mutable means we can change the content of list without changing its identity.
# we can add, remove, or modify elements in a list.
# kuch change hone orginal list bhi change ho jata hae
my_list3 = [1, 2, 3]
print('Before Modification:', my_list3)
my_list3[0] = 10  # modifying the first element
print('After Modification:', my_list3)
# we can add elements using append() method
my_list3.append(4)
print('After Appending:', my_list3)
# we can remove elements using remove() method
my_list3.remove(2)
print('After Removing:', my_list3)
# Lists are ordered, meaning the items have a defined order, and that order will not change unless you explicitly reorder the list.
#----------------------------------------------------------
# slice in list
my_list4 = [10, 20, 30, 40, 50]
print(my_list4[1:4])  # [20, 30, 40] (start index se leke end index-1 tak)
#----------------------------------------------------------
# list iteration
my_list5 = ['apple', 'banana', 'cherry']
# using for loop
for fruit in my_list5:
    print(fruit)
for i in range(0, len(my_list5)): # len(my_list5) = 3 --> range(0,3,1)
    print(my_list5[i])
#----------------------------------------------------------
# list methods
my_list6 = [5, 2, 9, 1, 5, 6]
my_list6.sort()  # sorts the list in ascending order
print('Sorted List:', my_list6)
my_list6.reverse()  # reverses the list
print('Reversed List:', my_list6)
index_of_5 = my_list6.index(5)  # finds the index of the first occurrence of 5
print('Index of 5:', index_of_5)
count_of_5 = my_list6.count(5)  # counts how many times 5 appears in the list
print('Count of 5:', count_of_5)
my_list6.insert(2, 15)  # inserts 15 at index 2
print('After Insertion:', my_list6)
my_list6.pop()  # removes and returns the last item
print('After Popping:', my_list6)
#----------------------------------------------------------

# Tuple
# Tuples are similar to lists, but they are immutable, meaning once a tuple is created, its content cannot be changed.
# You can create a tuple using parentheses () and separate items with commas.
# my_tuple = (10, 20, 30, 40, 50)
# print('Original Tuple:', my_tuple)
# why tuple is immutable?
# because once a tuple is created, its content cannot be changed.
# we cannot add, remove, or modify elements in a tuple.
# kuch change hone orginal tuple nahi change hota hae
# first way to create tuple
my_tuple2 = (1, 2, 3)
print('Before Attempted Modification:', my_tuple2)
# second way to create tuple
my_list_tuple = [4, 5, 6]
my_tuple3 = tuple(my_list_tuple)
print('Tuple from List:', my_tuple3)
# trying to modify tuple will raise an error
# my_tuple2[0] = 10  # This will raise a TypeError error is shown below
# TypeError: 'tuple' object does not support item assignment

#----------------------------------------------------------
ab=[1,2,3]

ba = ab # in here create a soft copy matlab ba and ab dono same memory location ko point kar rahe hae agar ab ya ba me koi bhi change karoge to dono me change ho jayega to avoid this is . we can use copy() method to create a deep copy
ba[0]=100
print(ab)  # [100, 2, 3]
print(ba)  # [100, 2, 3]
bc = ab.copy() # deep copy
bc[0]=500
print(ab)  # [100, 2, 3]
print(bc)  # [500, 2, 3]
#----------------------------------------------------------
# tuple iteration
my_tuple4 = ('apple', 'banana', 'cherry')
# using for loop
for fruit in my_tuple4:
    print(fruit)
for i in range(0, len(my_tuple4)): # len(my_tuple4) = 3 --> range(0,3,1)
    print(my_tuple4[i])
#----------------------------------------------------------
# tuple unpacking
my_tuple5 = (10, 20, 30)
a, b, c = my_tuple5  # unpacking the tuple into variables
print('a:', a)
print('b:', b)
print('c:', c)
#----------------------------------------------------------
# set  
# A set is an unordered collection of unique items in Python.
# Sets are mutable, meaning you can add or remove items from a set after its creation.
# You can create a set using curly braces {}  like in js me object hote python me set  hote  hae 
# set is also collection of items but the items are unique and unordered , unchangeable
myset={1,2,3,4,5}
print('Original Set:', myset) # output: {1, 2, 3, 4, 5}
myset2 = {1, 2, 2, 3, 4, 4, 5}  # duplicates will be removed automatically
print('Set with Duplicates Removed:', myset2) # {1, 2, 3, 4, 5}


#----------------------------------------------------------
# set is unordered hota hae mean that unordered ke andar koi bhi index work nahi karti  matlab set ke andar koi indexing work nahi kartei 
af={10,20,30,40,50}
# print(af[0]) # ye error dega is set object is not subscriptable matalb set andar nahi ja sakte hae 
for i in af:
    print(i)  # ye sahi hae set ke andar se item nikalne ke liye 1,2,3,4,5
#but agar apne esa kiya
# for i in range(0,len(af)): # ye error dega because set is not subscriptable
    # print(af[i])
#----------------------------------------------------------
# set methods
myset3 = {5, 2, 9, 1, 5, 6}
myset3.add(10)  # adds 10 to the set
print('After Adding 10:', myset3)
myset3.remove(2)  # removes 2 from the set
print('After Removing 2:', myset3)
myset3.discard(15)  # removes 15 from the set if present, does nothing if not present
print('After Discarding 15:', myset3)
#----------------------------------------------------------
# Dictionary
# Dictionaries is also like list  it is mutable  it is  iterable  but it has some sepcial powers and those are key value pairs
# diectionary like hasmap in other programming languages
diectionar={
    1:"apple",
    2:"banana",
    3:"cherry",
    4:"mango"
}


second_diectionar={
    "name":"john",
    "age":30,
    "city":"New York"
}
print(diectionar)
print(second_diectionar)
# accessing values in dictionary
print(diectionar[1])  # apple here 1 is key not index in dictionary we use key to access value
print(second_diectionar["name"])  # john
# modifying values in dictionary
diectionar[2] = "blueberry"
print(diectionar)  # {1: 'apple', 2: 'blueberry', 3: 'cherry', 4: 'mango'}
# adding new key-value pair
second_diectionar["job"] = "Engineer"
print(second_diectionar)  # {'name': 'john', 'age': 30, 'city': 'New York', 'job': 'Engineer'}
# removing key-value pair
del diectionar[3]
print(diectionar)  # {1: 'apple', 2: 'blueberry', 4: 'mango'}
# iterating through dictionary
for key in second_diectionar:
    print(key, ":", second_diectionar[key])
#----------------------------------------------------------
# dictionary methods

a ={198:10,2:200,3:300}
c = {5:500,6:600}
d ={ 3:900,4:400,7:700} 

a.update(c) # output will  be {198: 10, 2: 200, 3: 300, 5:500,6:600}  but if both dictionary has same key then the value of second dictionary will be taken
print(a)
a.update(d)
# print(a)  p-1 output will be {198:10,2:200,3:900,4:400,7:700}  value overide ho jayega jaha key same hogi
print(a)
#----------------------------------------------------------
# dictionary iternaiton 
for i in d:
    print(i,d[i])  # ye sahi hae set ke andar se item nikalne ke liye 1,2,3,4,5  i is key and d[i] is value here i is not a index