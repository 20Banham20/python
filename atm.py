def check_balance():
    pass

def withdraw():
    pass

def deposit():
    pass

def transaction_history():
    pass

pin=8967
x= True
attemps = 4

while x == True:
    user_pin_input = int(input("Please insert the pin:"))
    if user_pin_input == pin:
        print("Welcome to the ATM!\n")
        print("Please pick what you would like to do!")
        print(" 1.Check balance\n 2.Deposit\n 3.Withdraw\n 4.Transaction history\n 5.Exit")
    
        user_input= int(input("Please enter the number corresponding to your action:"))
    elif user_input == 1:
        check_balance()
    elif user_input == 2:
        withdraw()
    elif user_input == 3:
        deposit()
    elif user_input == 4:
        transaction_history()
    elif user_input == 5:
        break
    else:
        attemps -= 1
        if attemps >= 1:
            print (f"You have {attemps} left")
        else:
            break

            