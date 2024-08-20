
#decimal1=float(input("please give me a  decimal vaule to two dp"))
#decimal2=float(input("please give me another decimal vaule to two dp"))
#decimal3=(decimal1+decimal2 )
#print(f"{decimal3:.3f}")
#print("heres is your demical added together")

#name=str(input("whats your name"))
#color=str(input("whats your favourite color"))
#print(F"your name is:{name},and your color is {color}")

#temperature=int(input("please give me a temperature"))
#print("this is you temperature in fahrenheit")
#fahrenheit=1.8* temperature+32
#print(fahrenheit) 

#money=float(input("please give me a amount of money"))
#time=int(input("please give me a amount of years"))
#rate=float(input("please give me rate of interest"))
#result=(money*(1+rate)*time)
#print(f"{result:.5f}")

#name=str(input("please give me your full name"))
#age=int(input("please give me your age"))
#print(f"Hi{name} your have a great age as {age} ")

#password=str(input("please give me a password to enter"))
#right_password=(" height")

#if (password==right_password):
    #print("you may enter")
#else: 
    #print("Remove thy self from thee premises")

#age=int (input("Please enter you age"))
#age_even=(18)

#if (age==age_even):
    #print("you are old enough to watch are r-rated movies")
#else:
    #print(" you are not cool enough to watch r-rated movies")

#number=int(input("please give me a number"))

#if number %2 == 0:
    #print("Your number is even")
#else:
    #print("you number is odd")

#grade=int(input("Please input your grade"))

#if grade >=0 and grade <=30:
    #print("You got a not achieved")
#elif grade >=31 and grade <= 50:
    #print(" you got a achieved")
#elif grade >=51 and grade <=70:
   # print("you got a merit")
#elif grade >=71 and grade <=100:
    #print(" you got a excellence")
#else:
    #print("not a valid number")

#color=str(input("whats your favorite color"))

#if color=="blue":
    #print("Great choice!")
#else:
    #print("That's a nice color too!")

#number=int(input("please give me a number"))

#if number > 100:
    #print("That's a large number!")
#else:
    #print("That's a small number!")

#password=str(input("please give me a password to enter"))
#right_password=(" OpenSesame")

#if (password==right_password):
    #print("Access granted")
#else: 
   #print("Access denied")

#first_number=int(input("please give me a number"))
#Second_number=int(input("please give me a number"))

#sum=(first_number+Second_number)

#print (sum)

#number=int(input("please give me a number"))

#if number % 3 == 0 and number % 5 == 0:
    #print("FizzBuzz")
#elif number % 3 == 0:
 #print("Buzz")
#elif number % 5 ==0:
    #print("fizz")
#else:
    #print (number)

#height=int(input("please give me your height in centimeters"))

#if height >= 170:
    #print("you are tall enough to ride this roller coaster")
#elif height < 170:
    #print(" sorry you are not tall enough to ride this roller coaster")
#else:
    #print(" unknown height")

#number=int(input("please give me a number"))

#if number > 0:
    #print("you number is bigger than zero")
#elif number < 0:
    #print("you number is smaller than zero")
#else:
    #print("your number is equal to zero")

#birth_year=int(input("please give me your birth year"))

#age=2024-birth_year

#print(age)

#for i in range (1,11,1):
    #print(i)

#lis=[1,2,3,4,5]

#for i in lis:
    #print(i)

#lis=["apple","banana","cherry"]

#for i in lis:
    #print(i)

#for i in range (2,21,2):
    #print(i)

#word=str(input("please give me one word"))

#for i in word:
    #print(i)

#lis=[1,2,3,4,5]

#for i in lis:
    #print(i**2)

#for i in range (10,0,-1):
    #print(i)

#lis=["alice","bob","charlie"]

#for i in lis:
    #print(f"hello,{i}")

#lis=[10,20,30,40,50]

#for i in lis:
    #if i >= 25:
        #print(i)

#sen=str(input("please give me a sentence"))
#split=sen.split()

#for i in split:
    #print(i)

#fib=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#for i in fib:
    #print (i)
    
#lis=[70,85,90,75,60]

#for i in lis:
    #if i >= 70:
        #print(f"{i} is a passing grade")  
    #else:
        #print(f"{i} is a failing grade")
       
"""
def menu():
    print("Menu:")
    print("1. Pepperoni Pizza - $10")
    print("2. Cheese Pizza - $8")
    print("3. Veggie Pizza - $12")
    print("4. Beef & Onion - $15")
    print("5. Buger Pizz - $18")
    print("6. Meat lovers - $14")
    return

def order():
    order = []
    x = True
    while x == True:
        pizza_choice = input("Enter the number of the pizza you want to order (or 'done' to finish): ")
        if pizza_choice.lower() == 'done':
            x = False
        try:
            pizza_choice = int(pizza_choice)
            if 1 <= pizza_choice <= 6:
                order.append(pizza_choice)
            else:
                print("Invalid pizza choice. Please choose from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    return order

def total(order_list):
    cost = 0
    for pizza in order_list:
        if pizza == 1:
            cost += 10
        elif pizza == 2:
            cost += 8
        elif pizza == 3:
            cost += 12
        elif pizza == 4:
            cost += 15
        elif pizza == 5:
            cost += 18
        elif pizza == 6:
            cost += 14
    return cost
    
user_exit = False
while user_exit != True:
    print("Welcome to the Pizza Store!")
    print("Please pick what you would like to do!")
    print("1.Menu 2.Order 3.Calculate Total 4.Exit \n")
    user_input = int(input("Your choice boss: \n"))
    if user_input == 1:
        menu()
    elif user_input == 2:
        order_list = order()
        print("Your order:", order_list)
    elif user_input == 3:
        if order_list:
            total_cost = total(order_list)
            print("Your total is:", total_cost)
        else:
            print("Please place an order first.")
    elif user_input == 4:
        user_exit = True
        print("Thanks for stopping by!\n")

 """

#Write a function called remove_duplicates that takes a list as an argument and returns a new list with duplicate elements removed. 

#def remove_duplicates(ls):
    #new_ls=[]
    #for i in ls:
        #if i not in new_ls:
            #new_ls.append(i)
    #return new_ls

#try:
    #ls=[1,1,1,1,1,1,1,1,1,5,90,2,3,4,4,5,5,6]
    #new_ls=remove_duplicates(ls)
    #print(new_ls)
#except:
    #print("it didn't work")

"""
Problem Statement:
You are tasked with creating a Movie Rental System. The system should allow users to:
Add Movies: Add movies to the inventory.
Search Movies: Search for movies by title or genre.
Rent Movies: Rent out movies and update the inventory.
Return Movies: Return movies and update the inventory
Generate Rental Report: Provide a summary of rentals with the total revenue.
Requirements 
Movies can be stored in a list with just their titles. 
When a user rents a movie, the movie should be removed from the list
When a user returns a movie, it should be added back into the list
When a user wants to search for a movie they should type the movie title and 
A report should be generated for every movie that's been withdrawn or removed.
 
Your program should take user input, use variables and use if and else statements.
Loops (while and for) should be present. 
Functions should be used to break apart task and input validation must be present. 
Assume that there can only be one movie in the inventory at a time, there can be no duplicates. 
"""

"""

def add_movie():
    movies = ["ice age","end game","the joker","batman"]
    x = True
    print(movies)
    while x == True:
        add=str(input("Please input a movie or type '-1' when your \
finished:")).lower()
        if add == '-1':
            x = False
        else:
            movies.append(add)
            print(movies)
            x = True

def search_movie():
    x = True
    while x == True:
        find_movies=str(input("Please search for a movie:"))
        if find_movies in (movies):
            print(f"{find_movies} is available for rental")
        else:
            print("We do not have this movie")
            x=False

def rent_movie():
    user_active = True
    while user_active == True:
        user_input = str(input("Please type the movie you would like \
to rent or type 'done' when your finished:"))
        user_input = user_input.lower()
        if user_input == "done":
            user_active = False
        elif user_input in set (movies):
            print(f"You have now rented the movie:{user_input}")
            rented_list.append(rented_list)
            
        else:
            user_input = str(input("This movies doesn't exist would \
you like to try rent again?"))
            if user_input == 'Yes':
                print("Please try rent again")
                user_active = True
            else:
                user_active = False
            
def return_movie():
    user_active = True
    while user_active == True:
        user_input= str(input("Please type the movie you would like to \
reutrn or type 'done' when your finished:"))
        if user_input == "done":
            user_active = False
        elif user_input in set(movies):
            print(f"You have now returned the movie: {user_input}")
            return_list.append(return_list)
        else:
            user_input = str(input("This movies doesn't exist would \
you like to try return again?"))
            if user_input == 'Yes':
                print("Please try return again")
                user_active = True
            else:
                user_active = False

def rental_report():
    for i in rented_list:
        print("\n")
        print("This movie was rented:")
        print(i)
    for i in return_list:
        print("\n")
        print("this movie was returned:")
        print(i)

return_list = []
rented_list = []
movies = []
user_exit = False
while user_exit != True:
    print("Welcome to the Movies Reantals!")
    print("Please pick what you would like to do!")
    print("1.Add movie 2.Search movie 3.rent movie 4.return movie \
5.submit retal report \n")
    user_input = int(input("Your pick: \n"))
    if user_input == 1:
        movies=add_movie()
    elif user_input == 2:
        movies=search_movie()
    elif user_input == 3:
        if rent_movie:
            rent_movie()
        else:
            print("Please Add a movie first")
    elif user_input ==4:
        return_movie() 
    elif user_input == 5:
        rental_report()
        user_exit = True
        print("Thanks for stopping in!\n")

"""
"""
import random

def guess(x):
    
    Guess is the game where ypou guess 1-5
    
        number= random.randrange(1,5)
    user_guess = 0    
    win_conut = 0
    while user_guess <= 3:
            if x == 3:
                print ("please try win 5 times")
            if win_conut == 5:
                print("try again")
                break 
            if x == number:
                print("you have guessed the right number")
                user_guess += 3
                win_conut += 1
            if win_conut == 5:
                break
            if x != number:
                print("you have guess wrong")
                x = int(input('please guess another number (1-5): '))
                x + 1

           

num = int(input("please guess a number (1-5): "))
guess(num)






def addNumbers( a,b ) :
    """
    This adds vaules
    """

    result= a+b
    return result

def printMessage (name,age):
    """
    This will print their name and age
    """
    print("Hello, " + name + "! You are " + str(age) + " years old.")
    
def calcAreaCircle (r):
    """
    This will find the area of a circle
    """
    area=3.14*r*r
    return area

def checkAge(age): 
    """
    This will check if yours a adult
    """
    if age >= 18: 
        print("You are an adult.") 
    else: 
        print("You are a minor.")
  
# main program starts here
name="Alice";age=25
printMessage(name,age) # passes thourgh the name and age
checkAge(age)#passes through the age
x=10;y=20
sum = addNumbers(x,y)#passes through x and y
print("The sum is:",sum)
radius=5
area =calcAreaCircle(radius) #passes through the radius
print ("The area of the circle is:",area)


"""