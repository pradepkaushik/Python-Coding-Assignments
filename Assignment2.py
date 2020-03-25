
#QUESTION 1 -->


#THIS IS THE MESSAGE WE WANT TO PRINT OUT AT THE BEGINING

print("Welcome to the birthday dictionary.We know the birthdays of: Albert Einstein \nBenjamin Franklin\nAda Lovelace")

#WE HAVE CREATED A DICTIONARY NAME WITH BIRTHDAY

birthday_data = {"Albert Einstein" :"14/03/1879","Benjamin Franklin" :"17/01/1706","Ada Lovelace" :"10/12/1815"}

#CHECK CONDITION IF USER NAME MATCHES WITH OUR DATA OR NOT?

check = True

while check:

#WE HAVE TAKEN INPUT FROM USER

    whos_birthday = input("Who's birthday do you want to look up?: ")

    if whos_birthday == "Albert Einstein":

        print("Albert Einstein Birthday is {}".format(birthday_data["Albert Einstein"]))
        break

    elif whos_birthday == "Benjamin Franklin":

        print("Benjamin Franklin Birthday is {}".format(birthday_data["Benjamin Franklin"]))
        break

    elif whos_birthday == "Ada Lovelace":

        print("Ada Lovelace Birthday is {}".format(birthday_data["Ada Lovelace"]))
        break

    else:
        print("Please enter a valid name!")

        check = True

print()

