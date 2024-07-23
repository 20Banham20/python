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

 