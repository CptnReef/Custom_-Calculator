#This comment is to start the users choices in calculator.
print("carpe diem fool!\n")

#Fun Read to get the ball rolling!
print ("You're driving your car today and you have a bad~ feeling you can't shake off... \n Until it hits you! How many chicken crossed the road? \n it had to have been about 1-10\n")

#These variables are here to define the outcome this is important. If reach 0, end of the journey, man! If you can make it.

chickens = int(input())

#Assigning one car that you drive to hit the chickens
car = 1

# this is what add the questioning numbers together in order to begin.
crossing_road = chickens - car

#Assigning a variable text that shows it's 0
gameOver = "Nothing left\n"
#Ends with a questions

#condition if equation equals 0
if crossing_road <= 0:
    chickens0 = input("Why did the chicken died at the road?\n Type 'y' or 'n'")
    print(chickens0)
    if chickens0 == "y":
        print("to get to the otherside\n")

    else:
        print("ok\n")
        print("The Chickens are gone anyway...\n")
        print(gameOver)

# if these conditions are met: chickens greater than 0 and less than 10. This will perform.
if crossing_road >= 1 and crossing_road < 10:
    chickens1 = (input("The " + str(crossing_road) + " chicken(s) ran to the otherside... and into the desert! \n But wait?! 5 coyotes surrounds them for the pickings! \n will you keep watching? 'y' or 'n' \n"))
    leftOver = crossing_road
    print(chickens1)
    #Assign the number of coyotes
    coyote = 5
    #
    crossing_desert = leftOver - coyote
 
    if chickens1 == "y":
        if crossing_desert <= 0:
            print( "Only " + str(crossing_desert) + " left. Woof! I think they eat the bones too...")
        elif crossing_desert >= 1 and crossing_desert <= 5:
            print("At least there's " + str(crossing_desert) + " it made it back to the ranch to tell its story!")
        elif crossing_desert <= 6 and crossing_desert <= 10:
            print("Okay, there's " + str(crossing_desert) + " fate have mercy on these souls! Amen")
        # if these conditions are met: chickens > or = 0 this will prompt the ending
    else:
        print("the chickens was the last thing on your mind, so you left... Are you even human?!")

