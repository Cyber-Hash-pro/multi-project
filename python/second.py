# ------------------------------------------------------------
# control Flow (if/else)

# age = int(input('Enter age your'))
# print(age)
# : colom kya indentation ko active karta hae 
# what are the indentation  :-> 5 space deta hae like esa sjme ham if statement ke andar aa chuke hae LIKE {}
# if age>=18:
#     print('you can vote')
# else:
#     print("you can't vote")
# iam=''
# iam=[]
# # iam='apkesh'
# if '':
#     print('i am nilesh ')
# else :
#     print('i am not nilesh ')
# ------------------------------------------------------------
# nested if else
# item = input('which icercream do you have')
 
# if item=='pista':
#     print('pleace pack pista')
# elif item=='vanila':
#     print('ok pack vanila')
# elif item=='chocolate':
#     print('sorry we dont have chocolate')
# else:
#     print('we have only pista and vanila')
# -----------------------------------------------------------
# loop
# range(1,10,1)

# for loop always work on a counter/range function/number of itteration

# range() : -> this range function is used to generate a sequence of numbers
# syntax : -> range(start,stop,step)
# start : -> starting number of the sequence (inclusive)
# stop : -> ending number of the sequence (exclusive)
# step : -> difference between each number in the sequence (default is 1) like increment or decrement for increment +ve step and for decrement -ve step

# range(5,5,5) -> answer =[]
# range(1,10,2) -> answer =[1,3,5,7,9]
# LIKE JS for(let i=5; i<5; i++){
#     console.log(i);
# } PRINT THE NOTHING  BUT AGAR APNE I=5 ; I<6 ; I++  LIKH DIA TOH PRINT HO JAYEGA 5
# for i in range(5,6,5):
#     print(i)
# for i in range(9,91,9):
#     print(i)
# for rerver loop apko step me -ve value dena padega
# for i in range(10,0,-1):
#     print(i) --> prints 10 to 1
# ---------------------------------

#----------------------------------
#while
# a=0

# while a<10:
#     print(a)
#     a+=1  # a=a+1
# ---------------------------------
# break and continue
# for i in range(1,11):
#     if i==5:
#         break
#     print(i)
# ---------------------------------
# nested loop
for i in range(1,4):
    for j in range(1,4):
        print(i,j)
# ---------------------------------
 


