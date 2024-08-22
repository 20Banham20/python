def menu():
    amount = 0
    print("Welcome to the ATM!\n")
    print("Please pick what you would like to do!")
    print(" 1.Check balance\n 2.Withdraw\n 3.Deposit\n 4.Transaction history\n 5.Exit")
    user_input= int(input("Please enter the number corresponding to your action:"))

    if user_input == 1:
        check_balance(amount)
    elif user_input == 2:
        withdraw(amount)
    elif user_input == 3:
        deposit(amount)
    elif user_input == 4:
        transaction_history()
    elif user_input == 5:
        x=False

def check_balance(x):
    print(f"your balance is ${x}")
    menu(x)

def withdraw(x):
        user_input = float(input("please input the number you would like to withdraw:"))
        amount = x - user_input
        print(f"You have ${amount}")
        menu(x)

def deposit(x):
        user_input = float(input("please input the number you would like to deposit:"))
        amount = x + user_input
        print(f"You have ${amount}")
        menu(x)

def transaction_history():
    pass

pin=8967
x= True
attemps = 4

while x == True:
    user_pin_input = int(input("Please insert the pin:"))
    if user_pin_input == pin:
        menu()
        x = False
    else:
        attemps -= 1
        if attemps >= 1:
            print (f"You have {attemps} left")
        else:
            break
   
   

            