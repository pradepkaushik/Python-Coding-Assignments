# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 18:54:00 2019

@author: kaushik
"""

#QUESTION 1 -->

num=int(input("Enter number:")) #Here taking input from user
def factor_of_number(num):   #created a function here
    
   
    for i in range(1,num+1):  #checking input between given range
        
        if num%i ==0:
            
            if i % 2 ==0:   #again if condition for check odd/even
                
                print("Factor {} is even".format(i))
            else:
                print("Factor {} is odd".format(i))
                
factor_of_number(num)



#QUESTION 2 -->

#taking input from user as a string
sequence = input("enter your string:")

# we are assignning entered string into a test identifiers through split function
test1=sequence.split() 

test2= sorted(test1) # assignning sorted list into test2 identifiers

print(" ".join(test2))


#QUESTION 3 -->  

# not sure about this qus,you need even numbers or each digit to be even!

for num in range(999,3001): # we are running here a range between 1000 and 3000
    
    if num % 2 == 0:
    
        print(num,end=",")
print()



#QUESTION 4 -->

#taking an  input from user in a mixed string along with numbers

mix_string = input("Input a string:")

#assigning 0 values to two variables
Digits = 0
Letters = 0

for characters in mix_string:
    if characters.isdigit():  # built in funtion to check any digit inside it
        Digits += 1
    elif characters.isalpha(): # built in function to check characters inside it
        Letters += 1
    else:
        pass
print("Letters", Letters)
print("Digits", Digits)




#QUESTION 5 -->

#taking an input from user into integer 

pallindrome= int(input("Enter any number:"))

#assigning and converting its data type into string

num1 = str(pallindrome)
num2 = reversed(num1) # built in function to reveresed the string

if list(num1) == list(num2):  #comparison operator
    
    print("Number entered is pallindrome")
else:
    
    print("Number is not pallindrome")



#End of assignment!!!


