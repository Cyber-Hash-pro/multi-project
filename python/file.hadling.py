# file handling mean CRUD operation on file
# C- create a file and write data into it
# R- read data from file
# U- update data in file
# D- delete a file
# open() function is used to open a file in python
p = open(r'/home/cyber-rebel/Desktop/Portportfolio-website/README.md')
print(p) # here p is file object and it will print the file object

r = open('superman.txt','w')
r.write('i am super man ')
r.close() # here we are closing the file after writing data into it