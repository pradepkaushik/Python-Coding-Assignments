#ASSIGNMENT 4  -->

#QUE 1 AND QUESTION 10 SOLUTIONS ARE NOT PRESENT IN THIS


 #QUESTION 2 -->

#user has given a list of items

a = [4,7,3,2,5,9]

index =0   #taking index zero at initial stage

for items in a:    # for identifiers in iterable

    #format string,here first {} for items and {} for its index

    print("items at index {} is :{}".format(items,index))

    #index + 1 because we have to increase it each time when loop execute

    index+=1

print()



#QUESTION 3 -->

d = {"john":40, "peter":45}
print(list(d.keys()))


OUTPUT -- > ['john' , 'peter' ]



#QUESTION 4 -->

#taking input as a string from user,user must enter string with num digits

string = input("enter your string:")

for char in string:    #identifiers in iterable

    if not char.isdigit():   # isdigit for checking is there any number present in string

        print(char,end="")   #end="" to end any space between strings



#QUESTION 5 -->

#taking an input from user

user_string = input("enter string to be reversed:")

reverse_string = user_string[ : : -1] #negative index just to reversed the string in back

print(reverse_string)



#QUESTION 6 -->

list_1 = [1,3,6,78,35,55]

list_2 = [12,24,35,24,88,120,155]

result_list = []   #taking an empty list for storing result

for x in list_1:   # identifier in iterable list
    for y in list_2:
        result_list.append(x*y)   #appending result in new list

print(result_list)



#QUESTION 7 -->

a= [12,24,35,24,88,120,155]
new_list = [] #taking an emoty list for storing value
for item in a:

    if item !=24:   #checking each item in that list

        new_list.append(item)  #append elements apart from 24 into new list
print(new_list)


#QUESTION 8 -->

# I GUESS A WRONG WAY TO EXECUTE THIS QUESTION!!!!

a= [12,24,35,24,88,120,155]

a.pop(0),a.pop(3),a.pop(4)

print(a)


# MAY BE A CORRECT WAT FOR THIS !!!!!


my_list = [1,2,3,4,5,6,7]

#identifiers for identifiers in list and then if condition to check

my_list= [x for (i,x) in enumerate(my_list) if i not in (0,4,5)]

print(my_list)



#QUESTION 9 -->

a = [12,24,35,70,88,120,155]

#taken an empty string for storage purpose

new_list= []
for item in a: #identifiers in iterable

    if item % 5 != 0 and item % 7 != 0:

        new_list.append(item) #appending those items in that new list
print(new_list)

##NOTE -->
#I HAVEN'T TRIED QUE1 AND QUESTION 10 BECAUSE I COULDN'T UNDERSTAND THOSE QUESTIONS

#END OF ASSIGNMENT
