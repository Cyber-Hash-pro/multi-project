try:
 a = int(input("Enter a number: "))
 print(10/a) 
# except ZeroDivisionError:  # here kabhi kabhi kya erro aayega wo pata nahi chatal to hum use karte exe
    # print("You cannot divide a number by 0")
except Exception as e: # here agar koi bhi error aayega to wo e variable me store ho jayega
    print("An error occurred:", e) # here we can print the error message
else: # if except block me koi error nahi aaya to else block chalega and agar except block me error aaya to else block nahi chalega
    print("The division was successful") # here agar koi error nahi aaya to ye line print hogi
finally: # finally block hamesha chalega chahe except block me error aaye ya nahi
    print("This will always be executed") # here ye line hamesha print hogi chahe except block me error aaye ya nahi
print('agala code chla age 0 enter karne par error aayega  but baki code chla jayega or ye line print hoga ab try and except block ke baad ye line chalege ')

# slove is we have try except else finally  raise



# here if we enter 0 then it will give us an error because we cannot divide a number by 0
# here erro is agar numbe 0 hoga to error aayega because we cannot divide a number by 0
# to handle this error we can use try and except block
# 10/0 --> undefing nahi hae
# raise

age = int(input("Enter your age: "))
if age < 18:
    raise ValueError("You must be at least 18 years old to enter") # here we are raising a ValueError if the age is less than 18 and we are also providing a custom error message
else:
    print("Welcome to the party!") # here if the age is greater than or equal to 18 then we will print welcome to the party

print('the club is open for you') # here this line will be printed if the age is greater than or equal to 18 and if the age is less than 18 then this line will not be printed because we are raising an error and the program will stop executing after raising the error